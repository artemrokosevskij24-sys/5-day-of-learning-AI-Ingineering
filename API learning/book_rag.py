import os 
import chromadb
from google import genai 
from dotenv import load_dotenv

load_dotenv()

api_key=os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

class GeminiEmbeddingFunction(chromadb.EmbeddingFunction):
    def __call__(self, input=chromadb.Documents) -> chromadb.Embeddings:
        response = client.models.embed_content(
            model="gemini-embedding-001",
            contents=input
        )
        return [e.values for e in response.embeddings]

chroma_client = chromadb.Client()
custom_ef = GeminiEmbeddingFunction()

collection = chroma_client.create_collection(
    name="my_docs_gemini_files",
    embedding_function=custom_ef
)

collection.add(
    documents=["Космический корабль Икар отправляется в путешествие к далёкой звезде, а его экипаж хранит секрет, способный изменить будущее всего человечества.",
               "В далёком будущем, среди заброшенных станций на орбите Марса, инженер-андроид начинает задавать вопросы о собственном сознании.", 
               "Детектив Морган находит в старом особняке письмо с подсказкой, которая раскрывает личность убийцы спустя двадцать лет после преступления.", 
               "Расследование пропажи ценной картины приводит частного сыщика в мир антикваров, где каждый подозреваемый скрывает свою тайну.", 
               "Сборник рецептов итальянской кухни научит готовить классическую пасту карбонара и домашний тирамису всего за несколько простых шагов."],
    ids=["doc1", "doc2", "doc3", "doc4", "doc5"]
)

results = collection.query(
    query_texts=["что-то про космос"],
    n_results=2
)

found_docs = results["documents"][0]
context_text = "\n".join(found_docs)
user_question = "что то про космос"
final_prompt = f"контекст:\n{context_text}\n\nвопрос: {user_question}\n Ответь только на основе контекста выше."

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=final_prompt
)

print(response.text)




 

