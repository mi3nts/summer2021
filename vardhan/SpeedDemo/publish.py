import paho.mqtt.client as mqtt
from random import randrange, uniform
import time
import datetime

mqttBroker ="mqtt.eclipseprojects.io"

client = mqtt.Client("Speed")
client.connect(mqttBroker)

while True:
    current_time = datetime.datetime.now()
    randNumber = uniform(60, 70)
    client.publish("Speed", randNumber)
    print("Just published " + str(randNumber) + " to topic Speed" + " at time " + str(current_time))
    time.sleep(1)