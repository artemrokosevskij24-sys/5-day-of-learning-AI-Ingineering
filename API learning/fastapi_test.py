from fastapi import FastAPI
from pydantic import BaseModel
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

app = FastAPI()

class Question(BaseModel):
    text: str

@app.post("/ask")
def ask_question(question: Question):
     try:
        response = client.models.generate_content(model="gemini-3.5-flash", contents=question.text)
        return {"answer": response.text}
     except Exception as e:
        return {"error": "Сервис временно недоступен, попробуйте позже"}

@app.get("/")
def read_root():
    return {"message": "привет!"}