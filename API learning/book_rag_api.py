import os
import chromadb
from google import genai
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

class GeminiEmbeddingFunction(chromadb.EmbeddingFunction):
    def __call__(self, input=chromadb.Documents) -> chromadb.Embeddings:
        response = client.models.embed_content(
            model="gemini-embedding-001",
            contents=input
        )
        return [e.values for e in response.embeddings]      

collection = chromadb.Client().create_collection(name = "books", embedding_function=GeminiEmbeddingFunction())
collection.add(
    documents=["книга про космос", "книга про детектива"], 
    ids=["1", "2"]
)

app = FastAPI()

class Question(BaseModel):
    text: str

@app.post("/ask")
def ask(question: Question):
    results = collection.query(query_texts=[question.text], n_results=2)
    context_str = "\n".join(results["documents"][0])
    prompt = f"Контекст: {context_str}n\n\Вопрос: {question.text}"

    try:
        response = client.models.generate_content(model="gemini-3.5-flash", contents=prompt)
        return {"answer": response.text}
    except Exception as e:
        print(f"ошибка: {e}")
        return {"answer": "модель временно недоступна"}