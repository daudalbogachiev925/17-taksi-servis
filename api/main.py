from fastapi import FastAPI
from routes import tariffs, drivers, clients, trips, dispatch, reports

app = FastAPI(title="Taxi Service API")
app.include_router(tariffs.router, prefix="/tariffs", tags=["tariffs"])
app.include_router(drivers.router, prefix="/drivers", tags=["drivers"])
app.include_router(clients.router, prefix="/clients", tags=["clients"])
app.include_router(trips.router, prefix="/trips", tags=["trips"])
app.include_router(dispatch.router, prefix="/dispatch", tags=["dispatch"])
app.include_router(reports.router, prefix="/reports", tags=["reports"])

@app.get("/health")
def health(): return {"status": "ok"}
