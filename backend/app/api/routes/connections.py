from fastapi import APIRouter, Depends, HTTPException, status

from app.db.session import get_db
from app.schemas.connection import ConnectionCreate, ConnectionRead, ConnectionUpdate
from app.services import connections as service

router = APIRouter(prefix="/connections", tags=["connections"])


def get_connection_or_404(db, connection_id):
    connection = service.get_connection(db, connection_id)
    if connection is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Connection not found")
    return connection


@router.post("", response_model=ConnectionRead, status_code=status.HTTP_201_CREATED)
def create_connection(data: ConnectionCreate, db=Depends(get_db)):
    return service.create_connection(db, data)


@router.get("", response_model=list[ConnectionRead], status_code=status.HTTP_200_OK)
def list_connections(db=Depends(get_db)):
    return service.get_connections(db)


@router.get("/{connection_id}", response_model=ConnectionRead, status_code=status.HTTP_200_OK)
def get_connection(connection_id: int, db=Depends(get_db)):
    return get_connection_or_404(db, connection_id)


@router.patch("/{connection_id}", response_model=ConnectionRead, status_code=status.HTTP_200_OK)
def update_connection(connection_id: int, data: ConnectionUpdate, db=Depends(get_db)):
    connection = get_connection_or_404(db, connection_id)
    return service.update_connection(db, connection, data)


@router.delete("/{connection_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_connection(connection_id: int, db=Depends(get_db)):
    connection = get_connection_or_404(db, connection_id)
    service.delete_connection(db, connection)
