import logging
from kafka import KafkaProducer

# Configure logging
logger = logging.getLogger('KafkaProducerService')
logging.basicConfig(level=logging.INFO)

# Kafka Producer setup
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

def send_message(message: str):
    logger.info(f"Message sent -> {message}")
    producer.send('test', value=message.encode('utf-8'))
    producer.flush()

