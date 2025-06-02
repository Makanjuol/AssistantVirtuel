from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

from ApiRest.endpoints import upload, generation, synthesis, assistant  # transcription retiré

app = FastAPI(
    title="Assistant Vocal Intelligent",
    description="API REST pour assistant vocal (Transcription + GPT + Synthèse vocale)",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
"""app.include_router(upload.router, prefix="/audio", tags=["Upload audio"])
app.include_router(generation.router, prefix="/generate", tags=["Génération GPT"])
app.include_router(assistant.router, prefix="/assistant", tags=["Assistant vocal"])
"""
app.include_router(assistant.router, prefix="/assistant", tags=["Assistant vocal"])
app.include_router(synthesis.router, prefix="/speak", tags=["Synthèse vocale"])

# Interface web
app.mount("/", StaticFiles(directory="web_interface", html=True), name="static")

@app.get("/")
async def root():
    return RedirectResponse(url="/index.html")
