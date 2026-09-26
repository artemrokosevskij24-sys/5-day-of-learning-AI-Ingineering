import os 
from dotenv import load_dotenv
from google import genai

load_dotenv()

user_question = input("Задай свой вопрос: ")
print(f"Ты спросил: {user_question}")

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=user_question,
    config={
        "system_instruction": "Ты — дружелюбный ассистент, который отвечает кратко, максимум в 2-3 предложениях."
    }
)

print(response.text)