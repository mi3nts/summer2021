import paho.mqtt.client as mqtt
from random import randrange, uniform
import time

mqttBroker ="mqtt.eclipseprojects.io"

client = mqtt.Client("Speed")
client.connect(mqttBroker)

while True:
    randNumber = uniform(60, 70)
    client.publish("Speed", randNumber)
    print("Just published " + str(randNumber) + " to topic Speed")
    time.sleep(1)

