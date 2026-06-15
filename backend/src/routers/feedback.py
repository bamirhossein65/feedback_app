from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.auth.admin_auth import get_current_admin
from src.models.admin import Admin
from src.config.database import get_db
from src.schemas import feedback as schemas
from src import crud

router = APIRouter(prefix="/api/feedbacks", tags=["Feedbacks"])



# Routes for managing feedbacks
@router.post("/", response_model=schemas.FeedbackResponse)
def create_feedback(feedback: schemas.FeedbackCreate, db: Session = Depends(get_db)):
    return crud.create_feedback(db=db, feedback=feedback)

@router.get("/",response_model=List[schemas.FeedbackResponse],)
def read_feedbacks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin)
    ):
    return crud.get_feedbacks(db=db, skip=skip, limit=limit)

@router.patch("/{feedback_id}", response_model=schemas.FeedbackResponse)
def update_feedback_status(
    feedback_id: int,
    payload: schemas.FeedbackUpdateStatus,
    db: Session = Depends(get_db),
    current_admin: Admin = Depends(get_current_admin)
):
    if payload.status not in ["pending", "reviewed", "resolved"]:
        raise HTTPException(status_code=400, detail="Invalid status")
    updated_feedback = crud.update_feedback(db=db, feedback_id=feedback_id, status=payload.status)
    if not updated_feedback:
        raise HTTPException(status_code=404, detail="Feedback not found")
    return updated_feedback

@router.delete("/{feedback_id}")
def delete_feedback(feedback_id: int, db: Session = Depends(get_db)):
    success = crud.delete_feedback(db=db, feedback_id=feedback_id)
    if not success:
        raise HTTPException(status_code=404, detail="Feedback not found")
    return {"detail": "Feedback deleted successfully"}