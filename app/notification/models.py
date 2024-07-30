import uuid
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field

class Notification(BaseModel):
    __tablename__ = "notifications"
    notification_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    flight_id: Optional[str] = ''
    message: Optional[str] = ''
    timestamp: Optional[datetime] = None
    method: Optional[str] = ''
    recipient: Optional[str] = ''
