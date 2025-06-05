from fastapi import APIRouter, HTTPException, Path
from pydantic import BaseModel
from fastapi.responses import FileResponse
import pyttsx3
import os
from uuid import uuid4
from pydub import AudioSegment

router = APIRouter()

SYNTH_DIR = "response_audio"
os.makedirs(SYNTH_DIR, exist_ok=True)

class SynthesisRequest(BaseModel):
    text: str

class SynthesisResponse(BaseModel):
    audio_filename: str

# ✅ Fonction utilitaire réutilisable (ex: assistant.py, CLI, etc.)
def generate_speech(text: str) -> str:
    try:
        wav_filename = f"{uuid4()}.wav"
        wav_path = os.path.join(SYNTH_DIR, wav_filename)
        mp3_filename = wav_filename.replace(".wav", ".mp3")
        mp3_path = os.path.join(SYNTH_DIR, mp3_filename)

        engine = pyttsx3.init()
        engine.setProperty("rate", 170)
        engine.setProperty("volume", 1.0)

        # Choix voix française (si dispo)
        for voice in engine.getProperty("voices"):
            if "fr" in voice.name.lower():
                engine.setProperty("voice", voice.id)
                break

        engine.save_to_file(text, wav_path)
        engine.runAndWait()

        audio = AudioSegment.from_wav(wav_path)
        audio.export(mp3_path, format="mp3")
        os.remove(wav_path)

        return mp3_filename

    except Exception as e:
        raise RuntimeError(f"Erreur synthèse vocale : {e}")

# ✅ Route FastAPI
@router.post("/", response_model=SynthesisResponse, summary="Convertir un texte en audio (voix synthétique)")
def synthesize_speech(request: SynthesisRequest):
    try:
        audio_filename = generate_speech(request.text)
        return {"audio_filename": audio_filename}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur synthèse vocale : {e}")

@router.get("/file/{filename}", summary="Télécharger un fichier audio généré")
def get_audio_file(filename: str = Path(..., description="Nom du fichier audio")):
    path = os.path.join(SYNTH_DIR, filename)
    if not os.path.exists(path):
        raise HTTPException(status_code=404, detail="Fichier audio introuvable.")
    return FileResponse(path=path, media_type="audio/mpeg", filename=filename)
