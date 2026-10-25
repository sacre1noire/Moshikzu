from sqlalchemy import select

from app.core.errors import ConflictError
from app.models.finding import Finding

# Находки появляются только во время анализа или после его успешного завершения
RUN_STATUSES_ACCEPTING_FINDINGS = {"running", "done"}


def create_finding(db, run, data):
    if run.status not in RUN_STATUSES_ACCEPTING_FINDINGS:
        raise ConflictError(f"Cannot add findings to a {run.status} run")
    finding = Finding(run_id=run.id, **data.model_dump())
    db.add(finding)
    db.commit()
    db.refresh(finding)
    return finding


def get_findings(db, run_id):
    return db.scalars(
        select(Finding).where(Finding.run_id == run_id).order_by(Finding.id.desc())
    ).all()


def get_finding(db, finding_id):
    return db.get(Finding, finding_id)


def update_finding(db, finding, data):
    for key, value in data.model_dump(exclude_unset=True, exclude_none=True).items():
        setattr(finding, key, value)
    db.commit()
    db.refresh(finding)
    return finding


def delete_finding(db, finding):
    db.delete(finding)
    db.commit()
