import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

models_to_test = [
    "gemini-exp-1206",
    "gemini-2.0-flash-exp",
]

print("Testing experimental model availability...")

for model_name in models_to_test:
    print(f"\nTesting: {model_name}")
    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content("Hello")
        print(f"SUCCESS: {model_name} responded.")
        # break # Don't break, test both to see options
    except Exception as e:
        print(f"FAILED: {model_name} - {str(e)[:200]}...")
