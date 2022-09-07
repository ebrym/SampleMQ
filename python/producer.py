import pika

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.queue_declare(queue='letterbox')
message = "This is the reason i'm doin this."
channel.basic_publish(exchange='', routing_key='letterbox', body=message)

print(f"Message sent:{message}")
