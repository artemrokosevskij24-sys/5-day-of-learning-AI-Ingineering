import os
import numpy as np 
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

result1 = client.models.embed_content(model="gemini-embedding-001", contents="Сегодня утром я отлично пробежал пять километров по парку в тишине и прохладном воздухе.")
vector1 = result1.embeddings[0].values
result2 = client.models.embed_content(model="gemini-embedding-001", contents="Утренняя пробежка по аллеям парка зарядила меня бодростью и энергией на весь день.")
vector2 = result2.embeddings[0].values
result3 = client.models.embed_content(model="gemini-embedding-001", contents="Для стабильного FPS в играх нужно правильно настроить кривую вентиляторов и зафиксировать частоту процессора.")
vector3 = result3.embeddings[0].values

def cosine_similarity(a,b):
    return np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))
