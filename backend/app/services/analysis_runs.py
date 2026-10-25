from sqlalchemy import func, select

from app.core.errors import ConflictError
from app.models.analysis_run import AnalysisRun

FINISHED_STATUSES = {"done", "failed"}

# Из какого статуса в какие можно перейти: анализ идёт только вперёд
ALLOWED_TRANSITIONS = {
    "pending": {"running", "failed"},
    "running": {"done", "failed"},
    "done": set(),
    "failed": set(),
}


def create_run(db, connection_id):
    run = AnalysisRun(connection_id=connection_id, status="pending")
    db.add(run)
    db.commit()
    db.refresh(run)
    return run


def get_runs(db, connection_id):
    return db.scalars(
        select(AnalysisRun)
        .where(AnalysisRun.connection_id == connection_id)
        .order_by(AnalysisRun.id.desc())
    ).all()


def get_run(db, run_id):
    return db.get(AnalysisRun, run_id)


def update_run(db, run, data):
    changes = data.model_dump(exclude_unset=True, exclude_none=True)

    if run.status in FINISHED_STATUSES:
        raise ConflictError(f"Run is already {run.status} and cannot be changed")

    new_status = changes.get("status", run.status)
    if new_status != run.status and new_status not in ALLOWED_TRANSITIONS[run.status]:
        raise ConflictError(f"Cannot change status from {run.status} to {new_status}")

    if "tables_count" in changes and new_status != "done":
        raise ConflictError("tables_count can be set only when run becomes done")

    for key, value in changes.items():
        setattr(run, key, value)
    if new_status in FINISHED_STATUSES:
        run.finished_at = func.now()

    db.commit()
    db.refresh(run)
    return run


def delete_run(db, run):
    db.delete(run)
    db.commit()
