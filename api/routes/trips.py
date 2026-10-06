from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_session

router = APIRouter()

class TripIn(BaseModel):
    driver_id: int
    client_id: int
    tariff_id: int
    from_addr: str
    to_addr: str
    distance_km: float
    duration_min: int

@router.post("/")
def create(data: TripIn, db: Session = Depends(get_session)):
    tar = db.execute(text("SELECT base, per_km, per_min, min_fare FROM tariffs WHERE id=:i"),
                     {"i": data.tariff_id}).fetchone()
    if not tar: raise HTTPException(404, "Тариф не найден")
    price = tar[0] + tar[1]*data.distance_km + tar[2]*data.duration_min
    price = max(price, tar[3])
    commission = round(price * 0.20, 2)
    row = db.execute(text("""
        INSERT INTO trips (driver_id, client_id, tariff_id, from_addr, to_addr,
                           distance_km, duration_min, price, commission, status)
        VALUES (:driver_id,:client_id,:tariff_id,:from_addr,:to_addr,
                :distance_km,:duration_min,:price,:commission, 'in_progress')
        RETURNING id
    """), {**data.dict(), "price": price, "commission": commission}).fetchone()
    db.execute(text("UPDATE drivers SET available=FALSE WHERE id=:i"), {"i": data.driver_id})
    db.commit()
    return {"id": row[0], "price": float(price), "commission": float(commission)}

@router.post("/{trip_id}/finish")
def finish(trip_id: int, db: Session = Depends(get_session)):
    db.execute(text("""
        UPDATE trips SET status='done', finished=NOW() WHERE id=:i
    """), {"i": trip_id})
    db.execute(text("""
        UPDATE drivers SET available=TRUE
        WHERE id = (SELECT driver_id FROM trips WHERE id=:i)
    """), {"i": trip_id})
    db.commit()
    return {"status": "done"}

@router.post("/{trip_id}/cancel")
def cancel(trip_id: int, db: Session = Depends(get_session)):
    db.execute(text("UPDATE trips SET status='cancelled' WHERE id=:i"), {"i": trip_id})
    db.execute(text("""
        UPDATE drivers SET available=TRUE
        WHERE id = (SELECT driver_id FROM trips WHERE id=:i)
    """), {"i": trip_id})
    db.commit()
    return {"status": "cancelled"}
