from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_session

router = APIRouter()

class DIn(BaseModel):
    full_name: str
    phone: str | None = None
    car: str | None = None
    plate: str

@router.post("/")
def create(data: DIn, db: Session = Depends(get_session)):
    row = db.execute(text("""
        INSERT INTO drivers (full_name, phone, car, plate)
        VALUES (:full_name,:phone,:car,:plate) RETURNING id
    """), data.dict()).fetchone()
    db.commit()
    return {"id": row[0]}

@router.post("/{driver_id}/location")
def update_location(driver_id: int, lat: float, lon: float,
                    available: bool = True,
                    db: Session = Depends(get_session)):
    db.execute(text("""
        UPDATE drivers SET lat=:lat, lon=:lon, available=:a WHERE id=:i
    """), {"lat": lat, "lon": lon, "a": available, "i": driver_id})
    db.commit()
    return {"status": "updated"}

@router.get("/")
def list_all(available: bool | None = None, db: Session = Depends(get_session)):
    sql = "SELECT * FROM drivers WHERE status='active'"
    params = {}
    if available is not None:
        sql += " AND available = :a"
        params['a'] = available
    return [dict(r._mapping) for r in db.execute(text(sql), params).fetchall()]
