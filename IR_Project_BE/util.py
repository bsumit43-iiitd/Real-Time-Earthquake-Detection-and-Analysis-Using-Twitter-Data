
 

import logging
import socket

from confluent_kafka import Producer, Consumer



def create_producer():
    try:
        producer = Producer({"bootstrap.servers": 'localhost:9200',
                             "client.id": socket.gethostname(),
                             "enable.idempotence": True,  # EOS processing
                             "compression.type": "lz4",
                             "batch.size": 64000,
                             "linger.ms": 10,
                             "acks": "all",  # Wait for the leader and all ISR to send response back
                             "retries": 5,
                             "delivery.timeout.ms": 1000})  # Total time to make retries
    except Exception as e:
        logging.exception("Couldn't create the producer")
        producer = None
    return producer


def create_consumer(topic):
    try:
        consumer = Consumer({"bootstrap.servers": 'localhost:9200',
                             "client.id": socket.gethostname(),
                             "isolation.level": "read_committed",
                             "default.topic.config": {"auto.offset.reset": "latest", # Only consume new messages
                                                      "enable.auto.commit": False}
                             })

        consumer.subscribe([topic])
    except Exception as e:
        logging.exception("Couldn't create the consumer")
        consumer = None

    return consumer