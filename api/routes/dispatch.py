from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_session
from dispatch.dispatcher import dispatch

router = APIRouter()

@router.get("/nearest")
def nearest(lat: float, lon: float, max_km: float = 5,
            db: Session = Depends(get_session)):
    drivers = [dict(r._mapping) for r in db.execute(text("SELECT * FROM drivers WHERE available")).fetchall()]
    result = dispatch((lat, lon), drivers, max_km)
    return [{"id": d['id'], "name": d['full_name'], "distance": round(d['distance'], 3)}
            for d in result]
