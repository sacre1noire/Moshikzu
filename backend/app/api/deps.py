from fastapi import HTTPException, status

from app.services import connections as connection_service


def get_connection_or_404(db, connection_id):
    connection = connection_service.get_connection(db, connection_id)
    if connection is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Connection not found")
    return connection
