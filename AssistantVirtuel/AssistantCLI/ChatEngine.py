import os
import requests
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key) if openai_api_key else None

conversation_history = []

def ask_assistant(prompt: str) -> str:
    conversation_history.append({"role": "user", "content": prompt})

    # ✅ Essai GPT-3.5
    if client:
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=conversation_history
            )
            reply = response.choices[0].message.content.strip()
            conversation_history.append({"role": "assistant", "content": reply})
            print("🤖 GPT:", reply)
            return reply
        except Exception as e:
            print("⚠️ GPT indisponible :", e)

    # ✅ Essai DeepSeek local
    try:
        response = requests.post("http://localhost:11434/api/generate", json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        })

        if response.status_code == 200:
            reply = response.json()["response"].strip()
            conversation_history.append({"role": "assistant", "content": reply})
            print("🤖 DeepSeek:", reply)
            return reply
        else:
            print("⚠️ Réponse DeepSeek non valide")
    except Exception as e:
        print("⚠️ DeepSeek indisponible :", e)

    # ✅ Réponse fictive en dernier recours
    fallback_reply = "Je suis désolé, je ne peux pas répondre pour le moment. Essayez plus tard."
    conversation_history.append({"role": "assistant", "content": fallback_reply})
    print("🤖 Mode fictif :", fallback_reply)
    return fallback_reply
