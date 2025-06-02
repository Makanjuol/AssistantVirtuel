from pydantic import BaseModel

class AudioRequest(BaseModel):
    filename: str

class AudioResponse(BaseModel):
    transcription: str
    response_text: str
    response_audio_url: str  # ou path local si tu veux le servir depuis FastAPI
