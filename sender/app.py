import pika
import traceback
import time

credentials = pika.PlainCredentials('sender', 'sender')
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq-cluster',5672,'/',credentials)))
def Message():
  channel = connection.channel()
  channel.queue_declare(queue='hello')
  channel.basic_publish(exchange='',
                        routing_key='hello',
                        body='Hello World!')
  print(" [x] Sent 'Hello World!'")
  connection.close()

def every(delay):
  next_time = time.time() + delay
  while True:
    time.sleep(max(0, next_time - time.time()))
    try:
      Message()
    except Exception:
      traceback.print_exc()
    next_time += (time.time() - next_time) // delay * delay + delay

every(5)
