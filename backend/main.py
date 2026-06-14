from fastapi import FastAPI
from models import GenerateRequest
from prompt_engine import build_prompt
from db import add_project
import uuid

app = FastAPI()

# 🔥 MOCK AI VIDEO GENERATOR
def fake_ai_video(prompt: str):
    return {
        "video_url": "https://example.com/generated-video.mp4",
        "status": "success",
        "prompt_used": prompt
    }

@app.post("/generate")
def generate(req: GenerateRequest):
    prompt = build_prompt(req)
    result = fake_ai_video(prompt)

    project = {
        "id": str(uuid.uuid4()),
        "prompt": prompt,
        "settings": req.dict(),
        "result": result
    }

    add_project(project)
    return project


@app.get("/projects")
def get_projects():
    from db import load_db
    return load_db()
