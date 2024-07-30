import json
from app.utils.logger import logger
from config.config import get_kafka_config
from app.notification.routes import send_notification
from confluent_kafka import Consumer, KafkaException, KafkaError


class KafkaFlightConsumer:
    config = get_kafka_config()
    
    def __init__(self):
        self.conf = {
            'bootstrap.servers': f"{self.config['host']}:{self.config['port']}",
            'group.id': "flight_updates_group",
            'auto.offset.reset': 'earliest'
        }
        self.topic = self.config['topic']
        self.consumer = Consumer(self.conf)

    def consume_messages(self):
        self.consumer.subscribe([self.topic])
        logger.info('running kafka consumer...')
        try:
            while True:
                msg = self.consumer.poll(timeout=1.0)
                if msg is None:
                    continue
                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        continue
                    else:
                        logger.error(msg.error())
                        logger.error(KafkaException(msg.error()))
                message = json.loads(msg.value().decode('utf-8'))
                logger.info(f"Received message: {message}")
                send_notification(dict(message))

        except KeyboardInterrupt:
            pass
        finally:
            self.consumer.close()
