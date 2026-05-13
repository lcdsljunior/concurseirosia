import os
import google.generativeai as genai
from dotenv import load_dotenv
from core.prompts import SYSTEM_PROMPT

load_dotenv()

class EstudoAgente:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("API Key não encontrada!")
            
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(
            model_name=os.getenv("MODEL_NAME", "gemini-1.5-flash"),
            system_instruction=SYSTEM_PROMPT
        )
        self.chat = self.model.start_chat(history=[])

    def perguntar(self, mensagem):
        response = self.chat.send_message(mensagem)
        return response.text