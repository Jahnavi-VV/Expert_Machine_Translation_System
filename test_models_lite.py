import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

models_to_test = [
    "gemini-2.5-flash-lite",
    "gemini-2.5-flash-lite-preview-09-2025",
    "gemini-2.0-flash-lite-001",
]

print("Testing LITE model availability...")

for model_name in models_to_test:
    print(f"\nTesting: {model_name}")
    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content("Hello")
        print(f"SUCCESS: {model_name} responded.")
    except Exception as e:
        print(f"FAILED: {model_name} - {str(e)[:200]}...")
