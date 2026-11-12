import os
import shutil

from fastapi import FastAPI

app = FastAPI(title="Viral Spark Backend")


@app.get("/")
def root():
    return {
        "service": "Viral Spark Backend",
        "status": "running",
        "video_processing_ready": False,
    }


@app.get("/api/health")
def health():
    return {
        "status": "ok",
        "ffmpeg_available": shutil.which("ffmpeg") is not None,
        "hf_token_configured": bool(os.getenv("HF_TOKEN")),
        "video_processing_ready": False,
    }
