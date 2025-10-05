import json
from kafka import KafkaConsumer
from pymongo import MongoClient
from config import BOOTSTRAP_SERVERS, PROCESSED_TOPIC, MONGO_URI, MONGO_DB, MONGO_COLLECTION

consumer = KafkaConsumer(
    PROCESSED_TOPIC,
    bootstrap_servers=BOOTSTRAP_SERVERS,
    auto_offset_reset="earliest",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

client = MongoClient(MONGO_URI)
collection = client[MONGO_DB][MONGO_COLLECTION]

print("Consumer started...")

for msg in consumer:
    data = msg.value
    collection.insert_one(data)
    print("Saved to MongoDB:", data)
