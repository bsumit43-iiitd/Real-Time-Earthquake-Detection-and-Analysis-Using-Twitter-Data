
from time import sleep
from kafka import KafkaConsumer , KafkaProducer
from threading import Thread
import threading
import pandas as pd
from queue import Queue, Empty
import signal
import json
from predict import predict




emails = Queue()
is_shutting_down = False


class Consumer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        consumer = KafkaConsumer(
            "tweets", bootstrap_servers=["localhost:9092"], group_id="ir"
        )

      
        for message in consumer:
            self.insert_to_buffer(message.value)

            if is_shutting_down:
                break

        consumer.close()

    def insert_to_buffer(self, message):
        # print("received a message, inserting into a queue buffer")
        emails.put(message)


def parse_poll_message(batch):
    temp = []
    for msg in batch:
        temp.append(json.loads(msg.decode('utf-8')))
    # split_msg = list(row['text'].split('\t'))
    return temp


def process_messages():
    # print("processing message in queue buffer")

    temp_emails = []
    
    try:
        while True:
            temp_emails.append(emails.get_nowait())

    except Empty:
        pass
    

    df = pd.DataFrame(columns=['id','event','source','text'])
    
    temp = parse_poll_message(temp_emails)
    df = pd.DataFrame(temp)
    result = predict(df)
    print(f"Fetched Batch Result" )
    # print(result)
    producer = KafkaProducer( bootstrap_servers=["localhost:9092"])
    value = json.dumps(result).encode('utf-8')
    producer.send("locations", value=value)
    producer.close()

    # Define a function to handle a message event
   


def exit_gracefully(*args, **kwargs):
    global is_shutting_down
    is_shutting_down = True
    process_messages()
    exit()


def batch():

    # signal.signal(signal.SIGINT, exit_gracefully)
    # signal.signal(signal.SIGTERM, exit_gracefully)

    print("starting batch consumer worker")

    consumer = Consumer()
    consumer.daemon = True
    consumer.start()

    while True:
        process_messages()
        sleep(5)


consumer_thread = Thread(target=batch)
consumer_thread.start()