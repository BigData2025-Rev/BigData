from flask import Flask
from controllers.kafka_producer_controller import kafka_producer_controller

# Initialize Flask app
app = Flask(__name__)

# Register the controller blueprint
app.register_blueprint(kafka_producer_controller, url_prefix='/kafka')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

from services.kafka_consumer_service import consume

if __name__ == '__main__':
    consume()  # Start the Kafka consumer loop
