from jsonify import ticket_json
from confluent_kafka import Producer, KafkaError, KafkaException
import uuid


def producer():

    conf = {'bootstrap.servers': "pkc-epwny.eastus.azure.confluent.cloud:9092",
            'security.protocol': "sasl_ssl", 'sasl.mechanism': "PLAIN", 'sasl.username': "P4F3HOIJWDW4A6SG",
            'sasl.password': "UOee/3/dgupPKHQNlh/ZuoAomuVtD071uVFz9eRLynHqNscg76FWG9MslR/0mWqt"}

    producer = Producer(conf)

    def acked(err, msg):
        if err is not None:
            print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
        else:
            print("Message produced: %s" % (str(msg)))

    for j in ticket_json():
        # print(j)
        header = {}
        aggregateID = str(uuid.uuid4())
        header['type'] = "Core.Utilities.Application.Order.Events.OrderReceivedEvent"
        header['aggregate'] = aggregateID
        header['source'] = "Core.Utilities.Application.Order.Events.OrderReceivedEvent"
        producer.produce("Order-Service", key=aggregateID,
                         value=j, headers=header, callback=acked)
        producer.flush()
    # Wait up to 1 second for events. Callbacks will be invoked during
    # this method call if the message is acknowledged.
    producer.poll(1)
