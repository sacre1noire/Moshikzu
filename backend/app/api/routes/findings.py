from fastapi import APIRouter, Depends, status

from app.api.deps import get_finding_or_404, get_run_or_404
from app.db.session import get_db
from app.schemas.finding import FindingCreate, FindingRead, FindingUpdate
from app.services import findings as service

router = APIRouter(tags=["findings"])


@router.post(
    "/runs/{run_id}/findings",
    response_model=FindingRead,
    status_code=status.HTTP_201_CREATED,
)
def create_finding(run_id: int, data: FindingCreate, db=Depends(get_db)):
    run = get_run_or_404(db, run_id)
    return service.create_finding(db, run, data)


@router.get(
    "/runs/{run_id}/findings",
    response_model=list[FindingRead],
    status_code=status.HTTP_200_OK,
)
def list_findings(run_id: int, db=Depends(get_db)):
    get_run_or_404(db, run_id)
    return service.get_findings(db, run_id)


@router.get("/findings/{finding_id}", response_model=FindingRead, status_code=status.HTTP_200_OK)
def get_finding(finding_id: int, db=Depends(get_db)):
    return get_finding_or_404(db, finding_id)


@router.patch("/findings/{finding_id}", response_model=FindingRead, status_code=status.HTTP_200_OK)
def update_finding(finding_id: int, data: FindingUpdate, db=Depends(get_db)):
    finding = get_finding_or_404(db, finding_id)
    return service.update_finding(db, finding, data)


@router.delete("/findings/{finding_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_finding(finding_id: int, db=Depends(get_db)):
    finding = get_finding_or_404(db, finding_id)
    service.delete_finding(db, finding)
