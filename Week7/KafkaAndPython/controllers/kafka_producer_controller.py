from flask import Blueprint, request
from services.kafka_producer_service import send_message

# Initialize a Blueprint for the Kafka controller
kafka_producer_controller = Blueprint('kafka_producer_controller', __name__)

@kafka_producer_controller.route('/publish', methods=['POST'])
def send_message_to_kafka_topic():
    message = request.args.get('message')
    if message:
        print(f"Message: {message}")
        send_message(message)
        return 'Message published successfully!', 200
    else:
        return 'No message provided', 400

