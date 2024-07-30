from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class Flights(BaseModel):
    flight_id: str
    airline: str
    status: str
    departure_gate: str
    arrival_gate: str
    scheduled_departure: datetime
    scheduled_arrival: datetime
    actual_departure: Optional[datetime]
    actual_arrival: Optional[datetime]
