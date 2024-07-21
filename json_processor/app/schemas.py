from pydantic import BaseModel
from enum import Enum

class StateEnum(str, Enum):
    NEW = "NEW"
    INSTALLING = "INSTALLING"
    RUNNING = "RUNNING"

class ExampleBase(BaseModel):
    kind: str
    name: str
    version: str
    description: str = None
    state: StateEnum
    json: str

class ExampleCreate(ExampleBase):
    pass

class Example(ExampleBase):
    id: int

    class Config:
        orm_mode = True
