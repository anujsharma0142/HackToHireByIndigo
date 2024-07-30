from app.admin import schema
from app.utils.logger import logger
from app.admin.models import Flights
from app.db.connector import database_manager
from app.kafka.kafka_producer import KafkaProducer
from fastapi import APIRouter, HTTPException, Depends


postgres = database_manager.get_database()
router = APIRouter()
producer = KafkaProducer()

@router.get("/api/v1/get_all_flights", response_model=list[Flights])
async def all_flight_details():
    try:
        query = "SELECT * FROM flights"
        return await postgres.fetch_all(query)
    except Exception as e:
        logger.error(e)


@router.put("/api/v1/update_flight_status", response_model=Flights)
async def update_admin(flight: schema.FlightStatusUpdate):
    try:
        query = "UPDATE flights SET status = :status WHERE flight_id = :flight_id RETURNING *"
        values = {"flight_id": flight.flight_id, "status": flight.status}
        flight_data = await postgres.fetch_one(query, values)
        message = {
            'info': 'status_updated',
            'data': dict(flight_data)
        }
        message['data']['scheduled_departure']=str(message['data']['scheduled_departure'])
        message['data']['scheduled_arrival']=str(message['data']['scheduled_arrival'])
        producer.send_message(message=message)
        return flight_data
    except Exception as e:
        logger.error(e)


@router.put("/api/v1/update_flight_arrival_gate", response_model=Flights)
async def update_admin(flight: schema.FlightArrivalGateUpdate):
    try:
        query = "UPDATE flights SET arrival_gate = :arrival_gate WHERE flight_id = :flight_id RETURNING *"
        values = {"flight_id": flight.flight_id, "arrival_gate": flight.arrival_gate}
        flight_data = await postgres.fetch_one(query, values)
        message = {
            'info': 'status_updated',
            'data': dict(flight_data)
        }
        message['data']['scheduled_departure']=str(message['data']['scheduled_departure'])
        message['data']['scheduled_arrival']=str(message['data']['scheduled_arrival'])
        producer.send_message(message=message)
        return flight_data
    except Exception as e:
        logger.error(e)


@router.put("/api/v1/update_flight_departure_gate", response_model=Flights)
async def update_admin(flight: schema.FlightDepartureGateUpdate):
    try:
        query = "UPDATE flights SET departure_gate = :departure_gate WHERE flight_id = :flight_id RETURNING *"
        values = {"flight_id": flight.flight_id, "departure_gate": flight.departure_gate}
        flight_data = await postgres.fetch_one(query, values)
        message = {
            'info': 'status_updated',
            'data': dict(flight_data)
        }
        message['data']['scheduled_departure']=str(message['data']['scheduled_departure'])
        message['data']['scheduled_arrival']=str(message['data']['scheduled_arrival'])
        producer.send_message(message=message)
        return flight_data
    except Exception as e:
        logger.error(e)


@router.put("/api/v1/update_flight_scheduled_departure", response_model=Flights)
async def update_admin(flight: schema.FlightScheduledDepartureUpdate):
    try:
        query = "UPDATE flights SET scheduled_departure = :scheduled_departure WHERE flight_id = :flight_id RETURNING *"
        values = {"flight_id": flight.flight_id, "scheduled_departure": flight.scheduled_departure}
        flight_data = await postgres.fetch_one(query, values)
        message = {
            'info': 'status_updated',
            'data': dict(flight_data)
        }
        message['data']['scheduled_departure']=str(message['data']['scheduled_departure'])
        message['data']['scheduled_arrival']=str(message['data']['scheduled_arrival'])
        producer.send_message(message=message)
        return flight_data
    except Exception as e:
        logger.error(e)


@router.put("/api/v1/update_flight_scheduled_arrival", response_model=Flights)
async def update_admin(flight: schema.FlightScheduledArrivalUpdate):
    try:
        query = "UPDATE flights SET scheduled_arrival = :scheduled_arrival WHERE flight_id = :flight_id RETURNING *"
        values = {"flight_id": flight.flight_id, "scheduled_arrival": flight.scheduled_arrival}
        flight_data = await postgres.fetch_one(query, values)
        message = {
            'info': 'status_updated',
            'data': dict(flight_data)
        }
        message['data']['scheduled_departure']=str(message['data']['scheduled_departure'])
        message['data']['scheduled_arrival']=str(message['data']['scheduled_arrival'])
        producer.send_message(message=message)
        return flight_data
    except Exception as e:
        logger.error(e)