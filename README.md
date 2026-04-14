# Kafka Event-Driven Mini System

## Overview
This project demonstrates a simple event-driven architecture using Kafka.

## Architecture

Order Service → Kafka → Notification Service

## Components

### Order Service
- Flask API
- Sends order events to Kafka

### Notification Service
- Kafka consumer
- Prints received events

## Tech Stack
- Python
- Flask
- Kafka
- Docker (optional)

## How to Run

### 1. Start Kafka
docker-compose up -d

### 2. Start consumer
cd notification-service
python3 app.py

### 3. Start API
cd order-service
python3 app.py

### 4. Send test request
curl -X POST http://localhost:5001/order \
-H "Content-Type: application/json" \
-d '{"order_id": 1, "item": "coffee"}'

## What this demonstrates
- Event-driven architecture
- Decoupled microservices
- Kafka-based messaging
