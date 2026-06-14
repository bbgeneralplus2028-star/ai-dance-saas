from sqlalchemy import Column, String, JSON
from app.db import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(String, primary_key=True, index=True)
    prompt = Column(String)
    settings = Column(JSON)
    result = Column(JSON)
