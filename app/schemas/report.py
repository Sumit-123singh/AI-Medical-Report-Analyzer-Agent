from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ReportBase(BaseModel):
    title: str
    description: Optional[str] = None


class ReportCreate(ReportBase):
    pass


class ReportResponse(ReportBase):
    id: int
    user_id: int
    created_at: datetime
    analysis_result: Optional[str] = None

    class Config:
        from_attributes = True
