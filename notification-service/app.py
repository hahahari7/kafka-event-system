from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'orders',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='latest',   # 🔥 IMPORTANT CHANGE
    value_deserializer=lambda x: x.decode('utf-8')
)

print("👂 Listening for orders...")

for msg in consumer:
    print("RAW MESSAGE:", msg.value)

    try:
        data = json.loads(msg.value)
        print("📦 PARSED ORDER:", data)
    except Exception as e:
        print("⚠️ Skipped bad message")
