import json
from json import loads
from time import sleep
from kafka import KafkaConsumer, KafkaProducer
from flask import Flask
from flask import jsonify

def k_consumer():
  consumer = KafkaConsumer(group_id='f5-group', bootstrap_servers=['localhost:9092'], value_deserializer=lambda m: json.loads(m))
  consumer.subscribe(topics=['f5'])
  for message in consumer:
    foo = (message.value["virtualServers"]["/Demo_Application/nonsecure/serviceMain"])
    return jsonify(foo)

app = Flask(__name__)

@app.route('/')
def go():
  return k_consumer()

if __name__ == '__main__':
    app.run(host='0.0.0.0')

