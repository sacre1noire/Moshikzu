from fastapi import APIRouter, Depends, status

from app.api.deps import IdPath, get_connection_or_404, get_run_or_404
from app.db.session import get_db
from app.schemas.analysis_run import AnalysisRunRead, AnalysisRunUpdate
from app.services import analysis_runs as service

router = APIRouter(tags=["runs"])


@router.post(
    "/connections/{connection_id}/runs",
    response_model=AnalysisRunRead,
    status_code=status.HTTP_201_CREATED,
)
def create_run(connection_id: IdPath, db=Depends(get_db)):
    get_connection_or_404(db, connection_id)
    return service.create_run(db, connection_id)


@router.get(
    "/connections/{connection_id}/runs",
    response_model=list[AnalysisRunRead],
    status_code=status.HTTP_200_OK,
)
def list_runs(connection_id: IdPath, db=Depends(get_db)):
    get_connection_or_404(db, connection_id)
    return service.get_runs(db, connection_id)


@router.get("/runs/{run_id}", response_model=AnalysisRunRead, status_code=status.HTTP_200_OK)
def get_run(run_id: IdPath, db=Depends(get_db)):
    return get_run_or_404(db, run_id)


@router.patch("/runs/{run_id}", response_model=AnalysisRunRead, status_code=status.HTTP_200_OK)
def update_run(run_id: IdPath, data: AnalysisRunUpdate, db=Depends(get_db)):
    run = get_run_or_404(db, run_id)
    return service.update_run(db, run, data)


@router.delete("/runs/{run_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_run(run_id: IdPath, db=Depends(get_db)):
    run = get_run_or_404(db, run_id)
    service.delete_run(db, run)
