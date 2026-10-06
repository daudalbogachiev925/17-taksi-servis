from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_session

router = APIRouter()

class TIn(BaseModel):
    name: str
    base: float
    per_km: float
    per_min: float
    min_fare: float = 0

@router.post("/")
def create(data: TIn, db: Session = Depends(get_session)):
    row = db.execute(text("""
        INSERT INTO tariffs (name, base, per_km, per_min, min_fare)
        VALUES (:name,:base,:per_km,:per_min,:min_fare) RETURNING id
    """), data.dict()).fetchone()
    db.commit()
    return {"id": row[0]}

@router.get("/")
def list_all(db: Session = Depends(get_session)):
    return [dict(r._mapping) for r in db.execute(text("SELECT * FROM tariffs")).fetchall()]
