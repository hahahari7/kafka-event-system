from flask import Flask, request, jsonify
from kafka import KafkaProducer
import json

app = Flask(__name__)

# Kafka producer (IMPORTANT: localhost works because Kafka is running on your machine via Docker)
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

@app.route("/order", methods=["POST"])
def create_order():
    try:
        data = request.json

        if not data:
            return jsonify({"error": "No data sent"}), 400

        # send event to Kafka
        producer.send("orders", data)
        producer.flush()

        return jsonify({
            "status": "sent",
            "message": "Order published to Kafka",
            "data": data
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/")
def home():
    return "Order Service is running 🚀"


if __name__ == "__main__":
    app.run(port=5001, debug=True)
