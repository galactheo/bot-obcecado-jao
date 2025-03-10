# -*- coding: utf-8 -*-
"""bot_jao.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AdOF4ODaC3QRVgMQkTTTgpeCEJUfY8Zm
"""

from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai

app = Flask(__name__)

API_KEY = "---"

openai.api_key = API_KEY

def gerar_resposta(msg):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content":
             "Você é um fã fanático do Jão que conversa de maneira casual. "
             "Você só menciona Jão se fizer sentido no contexto, tentando forçar um pouco. "
             "As respostas devem ter até duas frases, podem incluir gírias e citar músicas ou curiosidades do Jão, mas não em todas as frases, apenas na maioria."
             "Não repita músicas e gírias imediatamente após uma mensagem"
             "Se perguntarem o que está fazendo no momento, peça para a pessoa adivinhar o que está ouvindo"},
            {"role": "user", "content": msg}
        ]
    )

    return response["choices"][0]["message"]["content"].strip()

@app.route("/bot", methods=["POST"])
def bot():
    msg = request.form.get("Body")
    print(f"Mensagem recebida: {msg}")  # Verifique se está chegando a mensagem
    resposta = gerar_resposta(msg)
    print(f"Resposta gerada: {resposta}")  # Verifique se está gerando a resposta

    twiml = MessagingResponse()
    twiml.message(resposta)
    return str(twiml)

if __name__ == "__main__":
    app.run(port=5000, debug=True)