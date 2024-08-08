import google.generativeai as genai

import os
from dotenv import load_dotenv

# os.environ.get('GOOGLE_API_KEY') without load_dotenv
load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

"""
Models
models/gemini-1.5-flash
models/gemini-1.5-pro-latest
models/gemini-1.5-pro
models/gemini-1.0-pro

"""
version = 'models/gemini-1.5-flash'
try:
    model = genai.GenerativeModel(version)
    prompt = "quien gano el ultimo mundial de futbol"
    response = model.generate_content(prompt)
    print(response.text)
except Exception as err:
    print(err)

#Chat Mode
print("Chat mode")
messages_list =[]
chat = model.start_chat(history=messages_list)
question1 = chat.send_message("Hola, a que distancia esta el sol?").text
question2 = chat.send_message("puedes crear palabras nuevas?").text


#chat history
print("Chat History:")
for message in chat.history:
    print(message)