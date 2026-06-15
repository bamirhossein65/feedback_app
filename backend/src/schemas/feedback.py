from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional

class FeedbackBase(BaseModel):
    name:Optional[str] = Field(None, max_length=100,description="نام فرستنده بازخورد")
    email: Optional[EmailStr] = Field(None, description="ایمیل فرستنده بازخورد")
    category: str = Field(..., max_length=50, description="دسته‌بندی بازخورد")
    message: str = Field(..., max_length=1000, description="متن بازخورد")

class FeedbackCreate(FeedbackBase):
    pass

class FeedbackUpdateStatus(BaseModel):
    status: str = Field(..., description="وضعیت جدید بازخورد")

class FeedbackResponse(FeedbackBase):
    id:int
    status:str
    created_at: datetime


    model_config = {"from_attributes": True}

