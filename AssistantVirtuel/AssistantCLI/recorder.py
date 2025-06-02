import speech_recognition as sr
from AssistantCLI.VoiceOutput import speak_text

def record_audio():
    """
    Enregistre l'audio via le micro et retourne l'objet audio.
    """
    listener = sr.Recognizer()
    microphone = sr.Microphone()

    # speak_text("Démarrer avec succès en quoi puis-je vous aider")
    print("🎙️ Parlez maintenant...")

    with microphone as source:
        listener.adjust_for_ambient_noise(source)
        audio = listener.listen(source)

    print("✅ Audio capturé.")
    return audio
