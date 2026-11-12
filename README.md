# Viral Spark Backend

Backend API for Viral Spark Studio.

## Current Status

This is an initial backend for deployment and connection testing.

It does not yet upload, transcribe, analyze, clip, or render videos.

## Technologies

- Python
- FastAPI
- Uvicorn
- Render for hosting

## Files

- main.py — FastAPI application and health-check endpoints.
- requirements.txt — Python dependencies.
- .gitignore — Files and folders excluded from Git.
- README.md — Project documentation.

## API Endpoints

### GET /

Returns basic server information and indicates that video processing
is not ready.

### GET /api/health

Returns:

- Server response status.
- Whether an FFmpeg executable is present.
- Whether the HF_TOKEN environment variable has a value.
- Whether video processing is ready.

The FFmpeg check does not test video rendering.
The token check does not validate the token or call Hugging Face.

## Render Deployment Settings

Service type: Web Service
Runtime: Python 3
Branch: main
Root directory: Leave empty

Build command:

    pip install -r requirements.txt

Start command:

    uvicorn main:app --host 0.0.0.0 --port $PORT

## Environment Variables

HF_TOKEN is optional for the current connection-test backend.

If needed later, configure it securely in Render.
Never put API keys, tokens, or passwords in repository files.

## Planned Features

These features are not implemented yet:

- Video uploads
- Audio transcription
- Highlight detection
- Clip selection
- Captions and vertical formatting
- Video rendering
- Downloadable video outputs

## Intended Connection

Lovable frontend → Render backend
GitHub repository → Backend code deployed on Render
