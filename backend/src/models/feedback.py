from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from src.config.database import Base

class Feedback(Base):
    __tablename__ = "feedbacks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    email = Column(String, nullable=True)
    category = Column(String, nullable=False)
    message = Column(String, nullable=False)
    status = Column(String(20),server_default="pending", nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())