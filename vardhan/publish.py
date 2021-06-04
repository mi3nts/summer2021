import paho.mqtt.client as mqtt
from random import randrange, uniform
import time
from datetime import datetime

mqttBroker ="mqtt.eclipseprojects.io"

client = mqtt.Client("Speed")
client.connect(mqttBroker)

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    randNumber = uniform(60, 70)
    client.publish("Speed", randNumber)
    print("Just published " + str(randNumber) + " to topic Speed" + " at time " + str(current_time))
    time.sleep(1)
