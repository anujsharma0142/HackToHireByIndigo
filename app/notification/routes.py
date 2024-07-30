import uuid
import asyncio
from fastapi import APIRouter
from datetime import datetime
from app.db.connector import database_manager
from app.utils.logger import logger
from app.utils.mail_service import MailService
from app.notification.models import Notification
from app.kafka.kafka_producer import KafkaProducer

postgres = database_manager.get_database()
router = APIRouter()
producer = KafkaProducer()


async def send_notification(message):
    print('got here in notification')
    timestamp = datetime.now()
    notification = {
        "notification_id":str(uuid.uuid4()),
        "flight_id":message['data']['flight_id'],
        "timestamp":timestamp, 
        "method":"email", 
        "recipient":"anujsharma0142@gmail.com"
    }
    if message['info'] == 'status_updated':
        notification['message'] = f'Your flight no {notification['flight_id']} is {message['data']['status']}'
    elif message['info'] == 'arrival_gate_updated':
        notification['message'] = f'Your fligth no {notification['flight_id']} is not arriving at gate no {message['data']['arrival_gate']}'
    elif message['info'] == 'departure_gate_updated':
        notification['message'] = f'Your fligth no {notification['flight_id']} is not departing from gate no {message['data']['departure_gate']}'
    elif message['info'] == 'scheduled_departure_updated':
        notification['message'] = f'Your fligth no {notification['flight_id']} departure time is updated. New departure time is {message['data']['scheduled_departure']}'
    elif message['info'] == 'scheduled_arrival_updated':
        notification['message'] = f'Your fligth no {notification['flight_id']} arrival time is updated. It will now arrive at {message['data']['scheduled_arrival']}'
    else:
        logger.error('Invalid info found in kafka messg')
        raise ValueError("Invalid info")
    
    query = """
        INSERT INTO notifications (notification_id, flight_id, message, timestamp, method, recipient)
        VALUES (:notification_id, :flight_id, :message, :timestamp, :method, :recipient)
    """
    await postgres.execute(query=query, values=notification)
    
    # email_service = MailService()
    # body = f"Hi, <br/>Your flight status has been updated<br/>{notification['message']}<br/><br/>This is a system generated mail, Do Not Reply"
    # email_service.send_email(subject="Flight Update", body=body, to_email=notification.recipient)

