from fastapi import HTTPException, status

from app.services import analysis_runs as run_service
from app.services import connections as connection_service
from app.services import findings as finding_service
from app.services import query_logs as query_log_service


def get_connection_or_404(db, connection_id):
    connection = connection_service.get_connection(db, connection_id)
    if connection is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Connection not found")
    return connection


def get_run_or_404(db, run_id):
    run = run_service.get_run(db, run_id)
    if run is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Run not found")
    return run


def get_finding_or_404(db, finding_id):
    finding = finding_service.get_finding(db, finding_id)
    if finding is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Finding not found")
    return finding


def get_query_log_or_404(db, entry_id):
    entry = query_log_service.get_entry(db, entry_id)
    if entry is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Query log entry not found")
    return entry
