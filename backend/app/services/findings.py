from sqlalchemy import select

from app.models.finding import Finding


def create_finding(db, run_id, data):
    finding = Finding(run_id=run_id, **data.model_dump())
    db.add(finding)
    db.commit()
    db.refresh(finding)
    return finding


def get_findings(db, run_id):
    return db.scalars(select(Finding).where(Finding.run_id == run_id)).all()


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
