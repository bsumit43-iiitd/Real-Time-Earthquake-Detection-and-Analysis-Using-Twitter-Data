from confluent_kafka import Consumer
import json

from predict import predict

KAFKA_BROKER_URL = 'localhost:9092'
live_data = []

def parse_poll_message(msg):
    row = json.loads(msg)
    split_msg = list(row['text'].split('\t'))
    return split_msg

consumer = Consumer({
    'bootstrap.servers': KAFKA_BROKER_URL,
    'group.id': 'ir',
    'auto.offset.reset': 'latest',
    'enable.auto.commit': True
})


consumer.subscribe(['tweets'])

while 1:
    msg = consumer.poll(200000)
    if msg is None:
        break
    elif msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue
    else:
        print(predict(parse_poll_message(msg.value().decode('utf-8'))))
        # live_data.append(parse_poll_message(msg.value().decode('utf-8')))


consumer.close()