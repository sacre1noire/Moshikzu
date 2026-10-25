from fastapi import APIRouter, Depends, status

from app.api.deps import get_connection_or_404, get_query_log_or_404
from app.db.session import get_db
from app.schemas.query_log_entry import QueryLogEntryCreate, QueryLogEntryRead, QueryLogEntryUpdate
from app.services import query_logs as service

router = APIRouter(tags=["query-logs"])


@router.post(
    "/connections/{connection_id}/query-logs",
    response_model=QueryLogEntryRead,
    status_code=status.HTTP_201_CREATED,
)
def create_entry(connection_id: int, data: QueryLogEntryCreate, db=Depends(get_db)):
    get_connection_or_404(db, connection_id)
    return service.create_entry(db, connection_id, data)


@router.get(
    "/connections/{connection_id}/query-logs",
    response_model=list[QueryLogEntryRead],
    status_code=status.HTTP_200_OK,
)
def list_entries(connection_id: int, db=Depends(get_db)):
    get_connection_or_404(db, connection_id)
    return service.get_entries(db, connection_id)


@router.get("/query-logs/{entry_id}", response_model=QueryLogEntryRead, status_code=status.HTTP_200_OK)
def get_entry(entry_id: int, db=Depends(get_db)):
    return get_query_log_or_404(db, entry_id)


@router.patch("/query-logs/{entry_id}", response_model=QueryLogEntryRead, status_code=status.HTTP_200_OK)
def update_entry(entry_id: int, data: QueryLogEntryUpdate, db=Depends(get_db)):
    entry = get_query_log_or_404(db, entry_id)
    return service.update_entry(db, entry, data)


@router.delete("/query-logs/{entry_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_entry(entry_id: int, db=Depends(get_db)):
    entry = get_query_log_or_404(db, entry_id)
    service.delete_entry(db, entry)
