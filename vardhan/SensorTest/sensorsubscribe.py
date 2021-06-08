import paho.mqtt.client as mqtt
from getmac import get_mac_address as gma
import time
import csv
import datetime
import json

macaddr = gma()
mac_csv = macaddr.replace(":", "")

#in actual implementation, all of the mac addresses here can be read in through f strings, not just copy and pasting
#initialize lists
Temperature = []
Pressure = []
Humidity = []
Altitude = []
fieldnames = ["dateTime", "Temperature", "Pressure", "Humidity", "Altitude"]


def on_message(client, userdata, message):
    current_time = datetime.datetime.now()
    if message.topic == f"{macaddr}/Temperature":
        print("Received message: " + str(message.payload.decode("utf-8")) + " at time " + str(current_time))
        Temperature.append(message.payload.decode("utf-8"))
    if message.topic == f"{macaddr}/Pressure":
        print("Received message: " + str(message.payload.decode("utf-8")) + " at time " + str(current_time))
        Pressure.append(message.payload.decode("utf-8"))
    if message.topic == f"{macaddr}/Humidity":
        print("Received message: " + str(message.payload.decode("utf-8")) + " at time " + str(current_time))
        Humidity.append(message.payload.decode("utf-8"))
    if message.topic == f"{macaddr}/Altitude":
        print("Received message: " + str(message.payload.decode("utf-8")) + " at time " + str(current_time))
        Altitude.append(message.payload.decode("utf-8"))

#random broker hosting
mqttBroker ="mqtt.eclipseprojects.io"

client = mqtt.Client("Database")
client.connect(mqttBroker)

#x_value = 0

#infinite loop that continuously sends data to csv
while True:
    client.loop_start()

    client.subscribe(f"{macaddr}/Temperature")
    client.subscribe(f"{macaddr}/Pressure")
    client.subscribe(f"{macaddr}/Humidity")
    client.subscribe(f"{macaddr}/Altitude")

    client.on_message = on_message


    with open(f"{mac_csv}_BME20.csv", 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        if (len(Altitude) == 0):
            info = {
                "dateTime": 0,
                "Temperature": 0,
                "Pressure" : 0,
                "Humidity" : 0,
                "Altitude" :0,
            }
        else:
            info = {
                "dateTime": str(datetime.datetime.now()),
                "Temperature": Temperature[-1],
                "Pressure": Pressure[-1],
                "Humidity": Humidity[-1],
                "Altitude": Altitude[-1],
            }
        csv_writer.writerow(info)

    data = {}

    if (len(Altitude) == 0):
        data["dateTime"] = 0
        data[f"{macaddr}/Temperature"] = 0
        data[f"{macaddr}/Pressure"] = 0
        data[f"{macaddr}/Humidity"] = 0
        data[f"{macaddr}/Altitude"] = 0
    else:
        data["dateTime"] = str(datetime.datetime.now())
        data[f"{macaddr}/Temperature"] = Temperature[-1]
        data[f"{macaddr}/Pressure"] = Pressure[-1]
        data[f"{macaddr}/Humidity"] = Humidity[-1]
        data[f"{macaddr}/Altitude"] = Altitude[-1]

    #write most recent data into json file
    with open("sensor.json", "w") as fp:
        json.dump(data, fp)


    time.sleep(1)
    client.loop_stop()
