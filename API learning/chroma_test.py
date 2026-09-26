import os
import chromadb
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

class GeminiEmbeddingFunction(chromadb.EmbeddingFunction):
    def __call__(self, input: chromadb.Documents) -> chromadb.Embeddings:
        response = client.models.embed_content(
            model="gemini-embedding-001",
            contents=input
        )
        return [e.values for e in response.embeddings]

chroma_client = chromadb.Client()
custom_ef = GeminiEmbeddingFunction()

collection = chroma_client.create_collection(
    name="my_docs_gemini",
    embedding_function=custom_ef
)

collection.add(
    documents=["Интенсивная кардиотренировка на беговой дорожке помогает эффективно сжигать калории и укреплять сердце.",
                "Сегодняшняя пробежка на свежем воздухе прошла отлично и дала мощный заряд бодрости на весь день.", 
                "Сочный стейк средней прожарки с пряными травами лучше всего сочетается с бокалом насыщенного красного вина.", 
                "Для приготовления нежной рыбы в сливочном соусе отлично подойдет свежее филе форели.", 
                "Тонкая настройка лимитов мощности процессора и мониторинг температур помогают избавиться от троттлинга в играх."],
    ids=["doc1", "doc2", "doc3", "doc4", "doc5"]
)

results = collection.query(
    query_texts=["что-то про бег"],
    n_results=2
)

found_docs = results["documents"][0]
context_text = "\n".join(found_docs)
user_question = "что то про бег"
final_prompt = f"Контекст:\n{context_text}\n\nВопрос: {user_question}\nОтветь только на основе контекста выше."

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=final_prompt
)

print(response.text)





