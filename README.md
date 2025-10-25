# DataEngineering-Assignment
Build a real-time data pipeline that fetches data from a public API (e.g., weather, cryptocurrency, or news), ingests it into Kafka, processes it using Kafka Streams, and stores the results in MongoDB, all running locally via Docker.

🔧 Tasks Summary:

Set up Docker containers for Kafka, Zookeeper, and MongoDB using docker-compose.yml.
Create a Kafka Producer that periodically pulls data from a public API (e.g., OpenWeatherMap, CoinGecko, or NewsAPI) and sends it to a Kafka topic (api-raw-data).
Implement Kafka Streams to filter, transform, or enrich the data (e.g., extract key fields, add tags, or compute metrics) and forward it to a new topic (api-processed-data).
Create a Kafka Consumer that reads from api-processed-data and inserts the records into MongoDB.
Verify data ingestion using MongoDB Compass or CLI.


🧪 Example Use Case:
Use the CoinGecko API to fetch live cryptocurrency prices, filter for Bitcoin and Ethereum, tag them with a timestamp and status, and store the results in MongoDB

  The final results should be uploaded to a GitHub repository, and the repository link must be shared in the attached Excel sheet.
