from sqlalchemy import select

from app.models.query_log_entry import QueryLogEntry


def create_entry(db, connection_id, data):
    entry = QueryLogEntry(connection_id=connection_id, **data.model_dump())
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry


def get_entries(db, connection_id):
    return db.scalars(select(QueryLogEntry).where(QueryLogEntry.connection_id == connection_id)).all()


def get_entry(db, entry_id):
    return db.get(QueryLogEntry, entry_id)


def update_entry(db, entry, data):
    for key, value in data.model_dump(exclude_unset=True, exclude_none=True).items():
        setattr(entry, key, value)
    db.commit()
    db.refresh(entry)
    return entry


def delete_entry(db, entry):
    db.delete(entry)
    db.commit()
