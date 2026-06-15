from sqlalchemy.orm import Session
from src.models import feedback as models
from src.schemas import feedback as schemas

def create_feedback(db:Session, feedback:schemas.FeedbackCreate):
    db_feedback = models.Feedback(
        name=feedback.name,
        email=feedback.email,
        category=feedback.category,
        message=feedback.message
    )
    db.add(db_feedback)
    db.commit()
    db.refresh(db_feedback)
    return db_feedback

def get_feedbacks(db:Session, skip:int=0, limit:int=100):
    return db.query(models.Feedback).order_by(models.Feedback.created_at.desc()).offset(skip).limit(limit).all()

def update_feedback(db:Session, feedback_id:int, status:str):
    db_feedback = db.query(models.Feedback).filter(models.Feedback.id == feedback_id).first()
    if db_feedback:
        db_feedback.status = status
        db.commit()
        db.refresh(db_feedback)
    return db_feedback

def delete_feedback(db:Session, feedback_id:int):
    db_feedback = db.query(models.Feedback).filter(models.Feedback.id == feedback_id).first()
    if db_feedback:
        db.delete(db_feedback)
        db.commit()
        return True
    return False