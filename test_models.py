import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

models_to_test = [
    "gemini-1.5-flash",
    "gemini-1.5-flash-001",
    "gemini-1.5-flash-002",
    "gemini-1.5-flash-8b",
    "gemini-1.0-pro"
]

print("Testing model availability and basic generation...")

for model_name in models_to_test:
    print(f"\nTesting: {model_name}")
    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content("Hello")
        print(f"SUCCESS: {model_name} responded.")
        break # Found a working one!
    except Exception as e:
        print(f"FAILED: {model_name} - {str(e)[:200]}...")
