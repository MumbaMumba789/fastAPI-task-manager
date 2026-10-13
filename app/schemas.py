from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    completed: bool = False

class TaskResponse(BaseModel):
    id: int
    title: str 
    description: str | None = None
    completed: bool

    class Config:
        # Crucial configuration to allow Pydantic to read raw SQLAlchemy objects
        from_attributes = True

class TaskUpdate(BaseModel):
    title: str | None = None 
    description: str | None = None 
    completed: bool | None = None
