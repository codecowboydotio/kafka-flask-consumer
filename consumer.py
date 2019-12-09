import json
from json import loads
from time import sleep
from kafka import KafkaConsumer, KafkaProducer
from flask import Flask
from flask import jsonify

def k_consumer():
  try:
    consumer = KafkaConsumer(group_id='None', auto_offset_reset='earliest', bootstrap_servers=['localhost:9092'], value_deserializer=lambda m: json.loads(m))
    consumer.subscribe(topics=['f5'])
    count=0
    for message in consumer:
      count +=1
      bitsin = (message.value["virtualServers"]["/Demo_Application/nonsecure/serviceMain"]["clientside.bitsIn"])
      bitsout = (message.value["virtualServers"]["/Demo_Application/nonsecure/serviceMain"]["clientside.bitsOut"])
      ccons = (message.value["virtualServers"]["/Demo_Application/nonsecure/serviceMain"]["clientside.curConns"])
      print message
  except:
    print("There was an error")

k_consumer()

