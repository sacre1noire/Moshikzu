from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import text

from app.api.routes import analysis_runs, connections, findings, query_logs
from app.db.session import get_db

app = FastAPI()
app.include_router(connections.router)
app.include_router(analysis_runs.router)
app.include_router(findings.router)
app.include_router(query_logs.router)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/health/db")
def health_check_db(db=Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "ok", "database": "reachable"}
    except Exception:
        raise HTTPException(status_code=503, detail="Database unreachable")
