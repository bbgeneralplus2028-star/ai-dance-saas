from fastapi import APIRouter
from app.prompt_engine import build_prompt
from app.services.ai_provider import generate_video
from app.services.storage import save_project, get_projects
from app.models import Project
import uuid

router = APIRouter()

@router.post("/generate")
def generate(data: dict):
    prompt = build_prompt(data)
    result = generate_video(prompt)

    project = Project(
        id=str(uuid.uuid4()),
        prompt=prompt,
        settings=data,
        result=result
    )

    save_project(project)

    return {"id": project.id, "result": result}


@router.get("/projects")
def projects():
    return get_projects()


@router.get("/health")
def health():
    return {"status": "ok"}
