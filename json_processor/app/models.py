from sqlalchemy import Column, Integer, String, Enum, Text
from .database import Base
import enum

class StateEnum(enum.Enum):
    NEW = "NEW"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"

class ExampleModel(Base):
    __tablename__ = "apps"

    id = Column(Integer, primary_key=True, index=True)
    kind = Column(String, nullable=False)
    name = Column(String, nullable=False)
    version = Column(String, nullable=True)
    description = Column(Text, nullable=True)
    state = Column(Enum(StateEnum), default=StateEnum.NEW, nullable=False)
    json = Column(Text, nullable=True)
