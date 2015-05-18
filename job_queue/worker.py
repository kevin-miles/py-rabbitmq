import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))
channel = connection.channel()
# RabbitMQ doesn't allow you to redefine an existing queue with different parameters
# and will return an error to any program that tries to do that.
channel.queue_declare(queue='job_durable', durable=True)

print ' [*] Waiting for messages. To exit press CTRL+C'
channel.start_consuming()


def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)
    time.sleep( body.count('.') )
    print " [x] Done"
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_consume(callback,
                      queue='job_durable')

channel.start_consuming()
