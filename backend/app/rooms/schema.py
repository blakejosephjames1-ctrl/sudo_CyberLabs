from typing import List
from pydantic import BaseModel, Field


class RoomTask(BaseModel):
    id: str = Field(..., description="Unique task identifier")
    description: str
    points: int = Field(..., ge=0)


class RoomDefinition(BaseModel):
    name: str
    difficulty: str
    description: str

    author: str
    version: str

    tasks: List[RoomTask]

    vm_templates: List[str]

    timeout_minutes: int = Field(..., gt=0)