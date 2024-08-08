from flask import Flask, render_template, request
from readcsv import readcsv
import signal
from kafka import KafkaConsumer
from threading import Thread
from readData import generateData
from batch import batch, exit_gracefully
from flask_socketio import SocketIO, emit
from map import createMap
# from batch import Consumer

app =   Flask(__name__)
app.config['SECRET_KEY'] = 'ir'
socketio = SocketIO(app, cors_allowed_origins='*')


@app.route('/')
def index():
    return generateData()

@socketio.on('connect')
def handle_connect():
    auth_header = request.headers.get('Authorization')
    # print(auth_header)
    token = auth_header.split(' ')[1] if auth_header else None
    
    # Authenticate client using token
    if token != 'ir':
        return False
    emit('message', 'Hello client!')


def start_consumer():
    print('Locations Extracted')
    # consumer = KafkaConsumer('locations', bootstrap_servers=['localhost:9092'])
    # for msg in consumer:
    #     html = createMap(msg.value.decode('utf-8'))
    #     print(html)
    #     print(msg.value.decode('utf-8'))
    #     socketio.emit('locations',  msg.value.decode('utf-8'))

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

@socketio.on('error')
def test_disconnect():
    print('Client disconnected')

if __name__ =="__main__":
    # signal.signal(signal.SIGINT, exit_gracefully)
    # signal.signal(signal.SIGTERM, exit_gracefully)
    # start_consumer()
    # app.run(host='127.0.0.1',port=8000, debug=True)
    # socketio.run(app,port=8000, debug=True)
    socketio.start_background_task(start_consumer)
    socketio.run(app, port=5000)
    consumer_thread = Thread(target=batch)
    consumer_thread.start()
    
