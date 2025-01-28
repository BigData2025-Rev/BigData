from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'test-topic',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='test-group',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

print("Consuming messages:")
for message in consumer:
    print(f"Received: {message.value}")

