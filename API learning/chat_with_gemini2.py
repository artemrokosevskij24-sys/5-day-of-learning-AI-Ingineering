import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

chat = client.chats.create(model="gemini-3.5-flash")

while True:
    user_question = input("Вопрос: ")
    if user_question == "стоп":
        break

    response = chat.send_message(user_question)
    print(response.text)
