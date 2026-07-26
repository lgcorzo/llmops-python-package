---
type: class
title: "FastAPIKafkaService"
source_path: "src/autogen_team/infrastructure/messaging/kafka_app.py"
description: "Service for deploying a FastAPI application with a Kafka producer and consumer."
tags: [class]
last_verified_commit: "dc137c3"
---

# FastAPIKafkaService

Source File: `src/autogen_team/infrastructure/messaging/kafka_app.py`

Service for deploying a FastAPI application with a Kafka producer and consumer.

## Architecture Visualization

```mermaid
classDiagram
    class FastAPIKafkaService {
        +prediction_callback
        +producer_config
        +consumer_config
        +input_topic
        +output_topic
        -__init__(prediction_callback, producer_config, consumer_config, input_topic, output_topic)
        +delivery_report(err, msg)
        +start()
        #_initialize_kafka_producer()
        #_initialize_kafka_consumer()
        #_run_server()
        #_consume_messages()
        #_poll_message()
        #_handle_message_error(msg)
        #_process_message(msg)
        #_close_consumer()
        +stop()
    }
```
