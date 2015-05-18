import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))
channel = connection.channel()
channel.queue_declare(queue='job')

print ' [*] Waiting for messages. To exit press CTRL+C'
channel.start_consuming()


def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)
    time.sleep( body.count('.') )
    print " [x] Done"

channel.basic_consume(callback,
                      queue='job',
                      no_ack=True)

channel.start_consuming()
