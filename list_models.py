import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    # Try finding it in secrets.toml if env var is missing (mimicking app logic simplified)
    import toml
    try:
        secrets = toml.load(".streamlit/secrets.toml")
        api_key = secrets.get("GOOGLE_API_KEY")
    except:
        pass

if not api_key:
    print("No API key found.")
else:
    genai.configure(api_key=api_key)
    try:
        print("Listing available 'flash' models:")
        for m in genai.list_models():
            if 'flash' in m.name:
                print(m.name)
        
        print("\nListing available 'pro' models:")
        for m in genai.list_models():
            if 'pro' in m.name:
                print(m.name)

    except Exception as e:
        print(f"Error: {e}")
