from fastapi import APIRouter, File, UploadFile
from fastapi.responses import JSONResponse
import os
from uuid import uuid4

router = APIRouter()

UPLOAD_DIR = "uploaded_audio"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/", summary="Uploader un fichier audio")
async def upload_audio(file: UploadFile = File(...)):
    """
    Enregistre un fichier audio envoyé par l'utilisateur.
    """
    try:
        file_extension = file.filename.split('.')[-1]
        unique_filename = f"{uuid4()}.{file_extension}"
        file_path = os.path.join(UPLOAD_DIR, unique_filename)

        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())

        return JSONResponse(
            status_code=200,
            content={"message": "Fichier reçu", "filename": unique_filename}
        )

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"message": f"Erreur pendant l’upload : {e}"}
        )
