import speech_recognition as sr

def transcribe_audio(audio_data):
    """
    Transcrit l'objet audio en texte à l'aide de Google Speech Recognition.
    
    Args:
        audio_data (sr.AudioData): L'objet audio à transcrire.
    
    Returns:
        str: Texte transcrit ou message d'erreur.
    """
    recognizer = sr.Recognizer()

    try:
        print("📝 Transcription en cours...")
        text = recognizer.recognize_google(audio_data, language="fr-FR")  # pour le français
        print("🗣️ Vous avez dit :", text)
        return text
    except sr.UnknownValueError:
        print("❌ Impossible de comprendre l'audio.")
        return "[Incompréhensible]"
    except sr.RequestError as e:
        print(f"❌ Erreur de requête Google Speech Recognition : {e}")
        return "[Erreur de transcription]"
