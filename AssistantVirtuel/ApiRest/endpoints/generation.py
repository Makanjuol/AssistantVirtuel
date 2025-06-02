
import os
import requests
from dotenv import load_dotenv
from fastapi import HTTPException
from openai import OpenAI
import re

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key) if openai_api_key else None

conversation_history = []


def ask_assistant(prompt: str) -> str:
    conversation_history.append({"role": "user", "content": prompt})

    # 🧠 1. GPT-3.5
    if client:
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=conversation_history,
                max_tokens=200
            )
            reply = response.choices[0].message.content.strip()
            reply = (reply)
            conversation_history.append({"role": "assistant", "content": reply})
            print("✅ Réponse GPT-3.5 :", reply)
            return reply
        except Exception as e:
            print("⚠️ GPT indisponible :", e)

    # 🧠 2. DeepSeek via Ollama
    try:
        response = requests.post("http://localhost:11434/api/generate", json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        })
        if response.status_code == 200:
            reply = response.json()["response"].strip()
            reply = (reply)
            conversation_history.append({"role": "assistant", "content": reply})
            print("✅ Réponse DeepSeek :", reply)
            return reply
        else:
            print("⚠️ DeepSeek a échoué :", response.text)
    except Exception as e:
        print("⚠️ DeepSeek indisponible :", e)

    # 🧠 3. Mode fictif
    fallback = "Désolé, je ne peux pas répondre pour le moment. Essayez plus tard."
    fallback = (fallback)
    conversation_history.append({"role": "assistant", "content": fallback})
    print("🛑 Mode fictif :", fallback)
    return fallback
