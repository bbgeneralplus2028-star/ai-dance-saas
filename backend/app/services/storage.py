from app.db import SessionLocal
from app.models import Project

def save_project(project):
    db = SessionLocal()
    db.add(project)
    db.commit()
    db.close()
    return project

def get_projects():
    db = SessionLocal()
    data = db.query(Project).all()
    db.close()
    return data
