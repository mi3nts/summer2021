from getmac import get_mac_address as gma
import paho.mqtt.client as mqtt
from collections import OrderedDict
from random import randrange, uniform
import time
import datetime
import json

macaddr = gma()
mac_topicname = macaddr.replace(":", "")


mqttBroker ="mqtt.eclipseprojects.io"
weathersensor = mqtt.Client("weathersensor")
rainsensor = mqtt.Client("rainsensor")
weathersensor_id = "BME20"
rainsensor_id = "GCCG41"

weathersensor.connect(mqttBroker)

while True:
    current_time = datetime.datetime.now()
    randTemperature = uniform(60, 70)
    randPressure = uniform(99820, 99835)
    randHumidity = uniform(80, 100)
    randAlt = uniform(125, 126)
    randRainfall = uniform(1, 12)
    randWindspeed = uniform(13, 20)
    weathersensorDictionary = OrderedDict([("dateTime", str(current_time)),
                                    ("Temperature", randTemperature),
                                    ("Pressure", randPressure),
                                    ("Humidity", randHumidity),
                                    ("Altitude", randAlt)])

    rainsensorDictionary = OrderedDict([("dateTime", str(current_time)),
                                        ("Rainfall", randRainfall),
                                        ("Windspeed", randWindspeed)])

    weathersensor.publish(f"{mac_topicname}/{weathersensor_id}", json.dumps(weathersensorDictionary))
    time.sleep(1)
    rainsensor.publish(f"{mac_topicname}/{rainsensor_id}", json.dumps(rainsensorDictionary))

    print("Just published " + str(randTemperature) + f" to topic {mac_topicname}/{weathersensor_id}, " + str(randPressure) + f" to topic {mac_topicname}/{weathersensor_id}, " + str(randHumidity) + f" to topic {mac_topicname}/{weathersensor_id}, " + str(randAlt) + f" to topic {mac_topicname}/{weathersensor_id} " + " at time " + str(current_time))
    print("Just published " + str(randRainfall) + f" to topic {mac_topicname}/{rainsensor_id}, " + str(randWindspeed) + f" to topic {mac_topicname}/{rainsensor_id} "+ "at time " + str(current_time))
    print("-"*10)

    time.sleep(1)
