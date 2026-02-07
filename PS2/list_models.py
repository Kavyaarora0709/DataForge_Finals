
import google.generativeai as genai
import os

API_KEY = "AIzaSyBnS0AaHj0mkFi2i3X0V_Clsp8SXVUNEX0"
genai.configure(api_key=API_KEY)

print("Listing available models...")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"- {m.name}")
except Exception as e:
    print(f"Error listing models: {e}")
