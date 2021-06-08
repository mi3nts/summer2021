import paho.mqtt.client as mqtt
import time
import csv
import datetime
import json


#initialize lists
speed_list_1 = []
fieldnames = ["x_value", "speed_data"]


def on_message(client, userdata, message, x_value = 1):
    current_time = datetime.datetime.now()
    print("Received message: " + str(message.payload.decode("utf-8")) + " at time " + str(current_time))
    speed_list_1.append(message.payload.decode("utf-8"))

#random broker hosting
mqttBroker ="mqtt.eclipseprojects.io"

client = mqtt.Client("Database")
client.connect(mqttBroker)

x_value = 0

#infinite loop that continuously sends data to csv
while True:
    client.loop_start()

    client.subscribe("Speed")
    client.on_message=on_message


    with open('SpeedDemo\data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        if (len(speed_list_1) == 0):
            info = {
                "x_value": 0,
                "speed_data": 0,
            }
        else:
            info = {
                "x_value": datetime.datetime.now(),
                "speed_data": speed_list_1[-1],
            }
        csv_writer.writerow(info)

    data = {}

    if (len(speed_list_1) == 0):
        data["Speed"] = 0
        data["Time"] = 0
    else:
        data["Speed"] = speed_list_1[-1]
        data["UTC"] = str(datetime.datetime.now())

    #write most recent data into json file
    with open("SpeedDemo\speed.json", "w") as fp:
        json.dump(data, fp)


    time.sleep(1)
    client.loop_stop()
#print(speed_list_1)


#out with the old, in with the new

# numbers = []
# speed_list = [float(x) for x in speed_list_1]
#
#
# for i in range (len(speed_list_1)):
#     numbers.append(i)
# plt.plot(numbers, speed_list)
# plt.title("Speed Vs. Time")
# plt.xlabel("Time")
# plt.ylabel("Speed")
# plt.show()