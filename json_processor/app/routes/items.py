from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, models, schemas
from ..database import SessionLocal, engine
from ..models import ExampleModel, StateEnum
from pydantic import BaseModel

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

class ExampleModelCreate(BaseModel):
    kind: str
    name: str
    version: str | None = None
    description: str | None = None
    state: StateEnum
    json: str | None = None

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/items")
def read_items():
    db = SessionLocal()
    items = db.query(ExampleModel).all()
    db.close()
    return items

@router.get("/items/{example_id}", response_model=schemas.Example)
def read_item(example_id: int, db: Session = Depends(get_db)):
    db_example = crud.get_example(db=db, example_id=example_id)
    if db_example is None:
        raise HTTPException(status_code=404, detail="Example not found")
    return db_example

@router.post("/items")
def create_item(item: ExampleModelCreate):
    db = SessionLocal()
    db_item = ExampleModel(
        kind=item.kind,
        name=item.name,
        version=item.version,
        description=item.description,
        state=item.state,
        json=item.json
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    db.close()
    return db_item




