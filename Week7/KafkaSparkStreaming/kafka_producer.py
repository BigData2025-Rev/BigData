from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic = 'test-topic'

for i in range(100):
    message = {'id': i, 'value': f'Message {i}'}
    producer.send(topic, message)
    print(f"Sent: {message}")
    time.sleep(1)

producer.flush()
producer.close()
