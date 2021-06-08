from getmac import get_mac_address as gma
import paho.mqtt.client as mqtt
from random import randrange, uniform
import time
import datetime

macaddr = gma()

mqttBroker ="mqtt.eclipseprojects.io"

sensor = mqtt.Client("sensor")

sensor.connect(mqttBroker)

while True:
    current_time = datetime.datetime.now()

    randTemperature = uniform(60, 70)
    randPressure = uniform(99820, 99835)
    randHumidity = uniform(80, 100)
    randAlt = uniform(125, 126)
    sensor.publish(f"{macaddr}/Temperature", randTemperature)
    sensor.publish(f"{macaddr}/Pressure", randPressure)
    sensor.publish(f"{macaddr}/Humidity", randHumidity)
    sensor.publish(f"{macaddr}/Altitude", randAlt)
    print("Just published " + str(randTemperature) + f" to topic {macaddr}/Temperature, " + str(randPressure) + f" to topic {macaddr}/Pressure, " + str(randHumidity) + f" to topic {macaddr}/Humidity, " + str(randAlt) + f" to topic {macaddr}/Altitude " + " at time " + str(current_time))
    time.sleep(1)
