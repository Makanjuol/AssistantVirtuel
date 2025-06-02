import os
import uuid
import speech_recognition as sr
from pydub import AudioSegment

# Répertoire temporaire
UPLOAD_DIR = "uploaded_audio"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def convert_to_wav(input_path: str) -> str:
    """
    Convertit n'importe quel fichier audio en format WAV lisible.
    """
    output_path = os.path.join(UPLOAD_DIR, f"{uuid.uuid4()}.wav")
    try:
        audio = AudioSegment.from_file(input_path)
        audio.export(output_path, format="wav")
        return output_path
    except Exception as e:
        raise RuntimeError(f"Erreur de conversion audio : {e}")

def transcribe_audio(file_path: str) -> str:
    """
    Transcrit un fichier audio (WAV uniquement) en texte.
    """
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data, language="fr-FR")
        return text
    except sr.UnknownValueError:
        raise RuntimeError("Impossible de comprendre l'audio.")
    except sr.RequestError as e:
        raise RuntimeError(f"Erreur API de transcription : {e}")
