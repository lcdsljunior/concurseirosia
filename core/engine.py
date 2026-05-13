import os
import google.generativeai as genai
from dotenv import load_dotenv
from core.prompts import SYSTEM_PROMPT

load_dotenv()

class EstudoAgentes:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        genai.configure(api_key=api_key)
        
        self.model = genai.GenerativeModel(
            model_name=os.getenv("MODEL_NAME"),
            system_instruction=SYSTEM_PROMPT
        )
        self.chat = self.model.start_chat(history=[])

    def perguntar(self, mensagem):
        response = self.chat.send_message(mensagem)
        return response.text