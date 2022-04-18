from json import dumps
from kafka import KafkaProducer
from kafka.errors import KafkaError

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

                        
for e in range(1000):
    data = {'number' : e, 'ip':'2.5.3.4', 'label':1,'@timestamp':'2022-01-25T17:27:01.734453'}
    producer.send('input-events', value=data)
