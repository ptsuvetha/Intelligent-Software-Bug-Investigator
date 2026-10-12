from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter(
    prefix="/investigate",
    tags=["Investigation"]
)


class InvestigationRequest(BaseModel):
    project_id: int
    bug: str


@router.post("/")
def investigate(request: InvestigationRequest):

    return {
        "status": "received",
        "project_id": request.project_id,
        "bug": request.bug,
        "message": "Investigation request received successfully"
    }
