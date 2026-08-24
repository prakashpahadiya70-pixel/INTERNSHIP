from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("❌ Gemini API key not found!")
    exit()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=api_key,
    temperature=0
)

response = llm.invoke("What is an AI Agent? Explain in one sentence.")

print("\n🤖 Gemini Response:")
print(response.content)