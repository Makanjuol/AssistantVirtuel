import sys
import os
import datetime
from AssistantCLI.recorder import record_audio
from AssistantCLI.transcriber import transcribe_audio

from AssistantCLI.ChatEngine import ask_assistant
from AssistantCLI.VoiceOutput import speak_text

def run_assistant():
    speak_text("Assistant Yèmi – En cours de démarrage...\n")

    while True:
        try:
            audio = record_audio()
            user_text = transcribe_audio(audio)
            
            if user_text.lower() in ["stop", "arrête toi", "ferme toi", "quitte", "exit", "quit"]:
                print("👋 Assistant terminé.")
                speak_text("Merci d'avoir utiliser Yèmi votre assistant, à bientôt")
                break

            response = ask_assistant(user_text)
            speak_text(response)
            print("\n---\n")

        except KeyboardInterrupt:
            print("\n🛑 Interruption par l'utilisateur.")
            speak_text("Merci d'avoir utiliser Yèmi votre assistant, à bientôt")
            break

if __name__ == "__main__":
    run_assistant()
