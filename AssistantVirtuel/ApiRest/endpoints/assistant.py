from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import shutil
import uuid
import os

from ApiRest.endpoints.transcription import convert_to_wav, transcribe_audio
from ApiRest.endpoints.generation import ask_assistant
from ApiRest.endpoints.synthesis import generate_speech  # ✅ fonction, pas route

router = APIRouter()
UPLOAD_DIR = "uploaded_audio"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/")
async def assistant(file: UploadFile = File(...)):
    # ✅ Étape 1 : sauvegarde temporaire du fichier uploadé
    file_ext = file.filename.split(".")[-1].lower()
    file_id = str(uuid.uuid4())
    raw_path = os.path.join(UPLOAD_DIR, f"{file_id}.{file_ext}")

    try:
        with open(raw_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur sauvegarde fichier : {e}")

    try:
        # ✅ Étape 2 : Conversion → WAV
        wav_path = convert_to_wav(raw_path)

        # ✅ Étape 3 : Transcription
        transcription = transcribe_audio(wav_path)
        if not transcription:
            raise HTTPException(status_code=400, detail="❌ Transcription échouée.")

        # ✅ Étape 4 : Génération de la réponse
        response_text = ask_assistant(transcription)

        # ✅ Étape 5 : Synthèse vocale avec fonction directe
        audio_filename = generate_speech(response_text)

        return JSONResponse(content={
            "transcription": transcription,
            "response_text": response_text,
            "audio_filename": audio_filename
        })

    except Exception as e:
        print(f"[❌ ERREUR DÉTAILLÉE] {e}")
        raise HTTPException(status_code=500, detail=str(e))
