import logging
from kafka import KafkaConsumer

# Configure logging
logger = logging.getLogger('KafkaConsumerService')
logging.basicConfig(level=logging.INFO)

# Kafka Consumer setup
consumer = KafkaConsumer(
    'test',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    group_id='test-group'
)

def consume():
    # Listen for messages from Kafka
    for message in consumer:
        logger.info(f"Message received -> {message.value.decode('utf-8')}")
