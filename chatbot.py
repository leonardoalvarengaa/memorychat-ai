import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

MODELO = "gemini-2.5-flash"

INSTRUCOES = """
Você é um assistente prestativo, inteligente e direto ao ponto.
Sempre responda em português.
"""

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def criar_chat():
    return client.chats.create(
        model=MODELO,
        config=types.GenerateContentConfig(
            system_instruction=INSTRUCOES
        ),
    )

chat = criar_chat()

def gerar_resposta(mensagem_usuario):
    try:
        resposta = chat.send_message(mensagem_usuario)
        return resposta.text

    except Exception as erro:
        return f"Erro: {erro}"