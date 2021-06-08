import paho.mqtt.client as mqtt
import time
import csv
import datetime
import json


#initialize lists
Temperature = []
Pressure = []
Humidity = []
Altitude = []
fieldnames = ["dateTime", "Temperature", "Pressure", "Humidity", "Altitude"]


def on_message(client, userdata, message):
    current_time = datetime.datetime.now()
    if message.topic == "4c:1d:96:a4:f7:0e/Temperature":
        print("Received message: " + str(message.payload.decode("utf-8")) + " at time " + str(current_time))
        Temperature.append(message.payload.decode("utf-8"))
    if message.topic == "4c:1d:96:a4:f7:0e/Pressure":
        print("Received message: " + str(message.payload.decode("utf-8")) + " at time " + str(current_time))
        Pressure.append(message.payload.decode("utf-8"))
    if message.topic == "4c:1d:96:a4:f7:0e/Humidity":
        print("Received message: " + str(message.payload.decode("utf-8")) + " at time " + str(current_time))
        Humidity.append(message.payload.decode("utf-8"))
    if message.topic == "4c:1d:96:a4:f7:0e/Altitude":
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

    client.subscribe("4c:1d:96:a4:f7:0e/Temperature")
    client.subscribe("4c:1d:96:a4:f7:0e/Pressure")
    client.subscribe("4c:1d:96:a4:f7:0e/Humidity")
    client.subscribe("4c:1d:96:a4:f7:0e/Altitude")

    client.on_message = on_message


    with open("4c1d96a4f70e_BME20.csv", 'a') as csv_file:
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
        data["Temperature"] = 0
        data["Pressure"] = 0
        data["Humidity"] = 0
        data["Altitude"] = 0
    else:
        data["dateTime"] = str(datetime.datetime.now())
        data["Temperature"] = Temperature[-1]
        data["Pressure"] = Pressure[-1]
        data["Humidity"] = Humidity[-1]
        data["Altitude"] = Altitude[-1]

    #write most recent data into json file
    with open("sensor.json", "w") as fp:
        json.dump(data, fp)


    time.sleep(1)
    client.loop_stop()