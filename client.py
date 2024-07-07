import pika
from pika import exceptions

try:
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='test_queue')

    channel.basic_publish(exchange='',
                          routing_key='test_queue',
                          body='Hello World!')

    print(" [x] Sent 'Hello World!'")

    connection.close()
except exceptions.AMQPConnectionError:
    print("AMQP Connection Error, Please Check Your RabbitMQ")
