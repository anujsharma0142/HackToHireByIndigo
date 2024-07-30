import json
from app.utils.logger import logger
from confluent_kafka import Producer 
from config.config import get_kafka_config


class KafkaProducer:
    config = get_kafka_config()

    def __init__(self):
        bootstrap_servers = f"{self.config['host']}:{self.config['port']}"
        self.producer = Producer({'bootstrap.servers': bootstrap_servers})

    def delivery_report(self, err, msg):
        if err is not None:
            logger.error(f"Message delivery failed: {err}")
        else:
            logger.info(f"Message delivered to {msg.topic()} [{msg.partition()}]")

    def send_message(self, message):
        logger.info(f'producing message {message}')
        self.producer.produce(self.config['topic'], key=str(message['data']['flight_id']), value=json.dumps(message), callback=self.delivery_report)
        self.producer.flush()
