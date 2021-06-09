import paho.mqtt.client as mqtt
from getmac import get_mac_address as gma
import time
import csv
import datetime
import json
import collections

macaddr = gma()
mac_name = macaddr.replace(":", "")
weathersensor_id = "BME20"
rainsensor_id = "GCCG41"


def on_message(client, userdata, message):
    decoder = json.JSONDecoder(object_pairs_hook=collections.OrderedDict)
    if message.topic == "4c1d96a4f70e/BME20":
        weathersensorDict = decoder.decode(message.payload.decode("utf-8","ignore"))
        print(str(weathersensorDict))
        with open(f"{mac_name}_{weathersensor_id}.json", "w") as fp:
            json.dump(message.payload.decode("utf-8"), fp)
        weather = []
        for key, value in weathersensorDict.items():
            weather.append(value)
        with open(f"{mac_name}_{weathersensor_id}.csv", "a") as outfile:
            csvwriter = csv.writer(outfile)
            csvwriter.writerow(weather)
        print("-"*20)
    elif message.topic == "4c1d96a4f70e/GCCG41":
        rainsensorDict = decoder.decode(message.payload.decode("utf-8", "ignore"))
        print(str(rainsensorDict))
        with open(f"{mac_name}_{rainsensor_id}.json", "w") as fp:
            json.dump(message.payload.decode("utf-8"), fp)
        rain = []
        for key, value in rainsensorDict.items():
            rain.append(value)
        with open(f"{mac_name}_{rainsensor_id}.csv", "a") as outfile:
            csvwriter = csv.writer(outfile)
            csvwriter.writerow(rain)


#random broker hosting
mqttBroker ="mqtt.eclipseprojects.io"

client = mqtt.Client("Database")
client.connect(mqttBroker)


#infinite loop that continuously sends data to csv
while True:
    client.loop_start()
    client.subscribe(f"{mac_name}/{weathersensor_id}")
    client.subscribe(f"{mac_name}/{rainsensor_id}")
    client.on_message = on_message

    # with open(f"{mac_name}_{weathersensor_id}.csv", 'a') as csv_file:
    #     csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    #     if (len(Altitude) == 0):
    #         info = {
    #             "dateTime": 0,
    #             "Temperature": 0,
    #             "Pressure" : 0,
    #             "Humidity" : 0,
    #             "Altitude" :0,
    #         }
    #     else:
    #         info = {
    #             "dateTime": str(datetime.datetime.now()),
    #             "Temperature": Temperature[-1],
    #             "Pressure": Pressure[-1],
    #             "Humidity": Humidity[-1],
    #             "Altitude": Altitude[-1],
    #         }
    #     csv_writer.writerow(info)

    time.sleep(1)
    client.loop_stop()
