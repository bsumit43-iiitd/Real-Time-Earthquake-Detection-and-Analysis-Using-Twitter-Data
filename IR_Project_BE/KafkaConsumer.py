# Import KafkaConsumer from Kafka library
from kafka import KafkaConsumer

# Import sys module
import sys

# Import json module to serialize data
import json
from multiprocessing import Process

def detect(index):
    # print(index)
    # Initialize consumer variable and set property for JSON decode
    consumer = KafkaConsumer ('tweets',bootstrap_servers = ['localhost:9092'],fetch_min_bytes=200000000,
    value_deserializer=lambda m: json.loads(m.decode('utf-8')))
    consumer.poll(100000000000)
    # print(consumer)
    # Read data from kafka
    list = []
    for message in consumer:
        list.append(message)
        print(len(list))

        # print("Consumer records:\n")
        # print(index)
        # print(message)
    # Terminate the script


for index in range(3):
    p = Process(target=detect(index))
    p.start()


sys.exit()
