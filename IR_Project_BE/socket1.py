from kafka import KafkaConsumer
from app import socketio

def start_consumer():
    consumer = KafkaConsumer('locations', bootstrap_servers=['localhost:9092'])

    for msg in consumer:
        print('HHHHHH')
        socketio.emit('message', {'data': msg.value.decode('utf-8')})