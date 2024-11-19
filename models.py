from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Task(BaseModel):
    id: int
    description: str
    status:str # "todo", "in-progress", or "done"
    createdAt: datetime
    updatedAt: Optional[datetime]
