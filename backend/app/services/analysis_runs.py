from sqlalchemy import select

from app.models.analysis_run import AnalysisRun


def create_run(db, connection_id, data):
    run = AnalysisRun(connection_id=connection_id, **data.model_dump())
    db.add(run)
    db.commit()
    db.refresh(run)
    return run


def get_runs(db, connection_id):
    return db.scalars(select(AnalysisRun).where(AnalysisRun.connection_id == connection_id)).all()


def get_run(db, run_id):
    return db.get(AnalysisRun, run_id)


def update_run(db, run, data):
    for key, value in data.model_dump(exclude_unset=True, exclude_none=True).items():
        setattr(run, key, value)
    db.commit()
    db.refresh(run)
    return run


def delete_run(db, run):
    db.delete(run)
    db.commit()
