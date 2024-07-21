import google.generativeai as genai

import os
from dotenv import load_dotenv
# os.environ.get('GOOGLE_API_KEY') without load_dotenv
load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

version = 'models/gemini-1.5-flash'
model = genai.GenerativeModel(version)
prompt = "Quien eres, responde detalladamente"
response = model.generate_content(prompt)
print(response.text)