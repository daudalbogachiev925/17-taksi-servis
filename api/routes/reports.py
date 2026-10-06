from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_session

router = APIRouter()

@router.get("/drivers")
def drivers(db: Session = Depends(get_session)):
    return [dict(r._mapping) for r in db.execute(text(open('sql/driver_kpi.sql').read())).fetchall()]

@router.get("/revenue")
def revenue(db: Session = Depends(get_session)):
    return [dict(r._mapping) for r in db.execute(text(open('sql/revenue.sql').read())).fetchall()]

@router.get("/commissions")
def commissions(db: Session = Depends(get_session)):
    return [dict(r._mapping) for r in db.execute(text(open('sql/commissions.sql').read())).fetchall()]

@router.get("/cancellations")
def cancellations(db: Session = Depends(get_session)):
    return [dict(r._mapping) for r in db.execute(text(open('sql/cancellations.sql').read())).fetchall()]

@router.get("/tariffs")
def tariffs(db: Session = Depends(get_session)):
    return [dict(r._mapping) for r in db.execute(text(open('sql/tariffs.sql').read())).fetchall()]
