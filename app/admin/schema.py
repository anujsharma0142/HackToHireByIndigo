from typing import Optional
from datetime import datetime
from pydantic import BaseModel

class FlightStatusUpdate(BaseModel):
    flight_id: str
    status: str


class FlightArrivalGateUpdate(BaseModel):
    flight_id: str
    arrival_gate: str


class FlightDepartureGateUpdate(BaseModel):
    flight_id: str
    departure_gate: str


class FlightScheduledArrivalUpdate(BaseModel):
    flight_id: str
    scheduled_arrival: Optional[datetime]


class FlightScheduledDepartureUpdate(BaseModel):
    flight_id: str
    scheduled_departure: Optional[datetime]
