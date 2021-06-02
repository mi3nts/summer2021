import paho.mqtt.client as mqtt
import time
import matplotlib.pyplot as plt

speed_list_1 = []

def on_message(client, userdata, message):
    print("received message: " ,str(message.payload.decode("utf-8")))
    speed_list_1.append(message.payload.decode("utf-8"))


mqttBroker ="mqtt.eclipseprojects.io"

client = mqtt.Client("Database")
client.connect(mqttBroker)

client.loop_start()

client.subscribe("Speed")
client.on_message=on_message

time.sleep(30)
client.loop_stop()

import matplotlib.pyplot as plt

numbers = []

speed_list = [float(x) for x in speed_list_1]


for i in range (len(speed_list_1)):
    numbers.append(i)
plt.plot(numbers, speed_list)
plt.title("Speed Vs. Time")
plt.xlabel("Time")
plt.ylabel("Speed")
plt.show()