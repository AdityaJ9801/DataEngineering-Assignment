import requests, json, time
from kafka import KafkaProducer
from config import BOOTSTRAP_SERVERS, PROCESSED_TOPIC

producer = KafkaProducer(
    bootstrap_servers=BOOTSTRAP_SERVERS,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

while True:
    try:
        # Fetch data from CoinGecko
        data = requests.get(
            "https://api.coingecko.com/api/v3/simple/price",
            params={"ids":"bitcoin,ethereum","vs_currencies":"usd"}
        ).json()

        # Transform each coin into a record
        for coin, val in data.items():
            record = {"coin": coin, "usd_price": val["usd"], "tag": "crypto-stream"}
            producer.send(PROCESSED_TOPIC, record)
            print("Produced:", record)

        producer.flush()  # ensure messages are sent
    except Exception as e:
        print("Producer error:", e)

    time.sleep(10)
