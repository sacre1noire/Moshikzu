from sqlalchemy import select

from app.models.connection import Connection


def create_connection(db, data):
    connection = Connection(**data.model_dump())
    db.add(connection)
    db.commit()
    db.refresh(connection)
    return connection


def get_connections(db):
    return db.scalars(select(Connection).order_by(Connection.id.desc())).all()


def get_connection(db, connection_id):
    return db.get(Connection, connection_id)


def update_connection(db, connection, data):
    for key, value in data.model_dump(exclude_unset=True, exclude_none=True).items():
        setattr(connection, key, value)
    db.commit()
    db.refresh(connection)
    return connection


def delete_connection(db, connection):
    db.delete(connection)
    db.commit()
