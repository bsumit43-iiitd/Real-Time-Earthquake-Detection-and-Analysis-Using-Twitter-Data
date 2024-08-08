from flask import Flask, render_template, request
import signal
import json
import threading
import time
from kafka import KafkaConsumer
from threading import Thread
from flask_socketio import SocketIO, emit
from map import createMap
loc_arr=[]
interval = 30 
app =   Flask(__name__)
app.config['SECRET_KEY'] = 'ir'
socketio = SocketIO(app, cors_allowed_origins='*')


@app.route('/')
def index():
    return 'Hello'

@socketio.on('connect')
def handle_connect():
    auth_header = request.headers.get('Authorization')
    print(auth_header)
    token = auth_header.split(' ')[1] if auth_header else None
    
    # Authenticate client using token
    if token != 'ir':
        return False
    emit('message', 'Hello client!')


def start_consumer():
    consumer = KafkaConsumer('locations', bootstrap_servers=['localhost:9092'])
    for msg in consumer:
        # loc_arr.extend(json.loads(msg.value.decode('utf-8')))
        # print(json.loads(msg.value.decode('utf-8')))
        # for i in json.loads(msg.value.decode('utf-8')):
        #     print(i)
        # print(json.loads(msg.value.decode('utf-8')))
        loc_arr.extend(json.loads(msg.value.decode('utf-8')))

def callMap():
    global loc_arr
    loc=[]
    loc=loc_arr
    loc_arr=[]
    try:
            html = createMap(loc, socketio)
            # html = createMap(loc_arr)
            # print(html)
            # print(msg.value.decode('utf-8'))
            socketio.emit('map',  html)
    except Exception as e:
            print(e)
            print("An exception occurred")

def run_function_every_30_seconds():
    threading.Timer(10.0, run_function_every_30_seconds).start()
    main_thread = threading.Thread(target= callMap)
    main_thread.start()

run_function_every_30_seconds()
   


@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

@socketio.on('error')
def test_disconnect():
    print('Client disconnected')

if __name__ =="__main__":
    socketio.start_background_task(start_consumer)
    socketio.run(app, port=8001)
    # time.sleep(10)
    # run_function_every_30_seconds()
    
