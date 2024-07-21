from sqlalchemy.orm import Session
from . import models, schemas

def get_example(db: Session, example_id: int):
    return db.query(models.ExampleModel).filter(models.ExampleModel.id == example_id).first()

def create_example(db: Session, example: schemas.ExampleCreate):
    db_example = models.ExampleModel(**example.dict())
    db.add(db_example)
    db.commit()
    db.refresh(db_example)
    return db_example
