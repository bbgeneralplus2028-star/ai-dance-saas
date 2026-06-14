from pydantic import BaseModel
from typing import Optional, List

class GenerateRequest(BaseModel):
    style: str
    expression: str
    background: str
    effects: List[str] = []
    camera: str
    aspect_ratio: str
    batch: bool = False
