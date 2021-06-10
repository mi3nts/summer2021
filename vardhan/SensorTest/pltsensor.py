import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import datetime

index = count()
fig, (ax1, ax2) = plt.subplots(2, 1)
xticklabels = []

def animate(i):
    datarain = pd.read_csv("4c1d96a4f70e_GCCG41.csv")
    dataweather = pd.read_csv("4c1d96a4f70e_BME20.csv")

    dateTimerain = datarain["dateTime"]
    rainfall = datarain["Rainfall"]
    windspeed = datarain["Windspeed"]

    dateTimeweather = dataweather["dateTime"]
    Temperature = dataweather["Temperature"]
    Pressure = dataweather["Pressure"]
    Humidity = dataweather["Humidity"]
    Altitude = dataweather["Altitude"]

    ax1.cla()
    ax2.cla()


    ax1.plot(dateTimerain, rainfall, label="rainfall")
    ax1.plot(dateTimerain, windspeed, label="windspeed")

    ax1.title.set_text("rainsensor data")
    ax1.legend(loc="upper left")
    ax1.set_xlabel("UTC Time")
    ax1.set_ylabel("rainfall/windspeed")


    ax2.title.set_text("weathersensor data")
    ax2.plot(dateTimeweather, Temperature, label="Temperature")
    ax2.plot(dateTimeweather, Pressure, label="Pressure")
    ax2.plot(dateTimeweather, Humidity, label="Humidity")
    ax2.plot(dateTimeweather, Altitude, label="Altitude")
    plt.tight_layout()

    ax2.title.set_text("weathersensor data")
    ax2.legend(loc="upper left", prop={"size":8})
    ax2.set_xlabel("UTC Time")
    ax2.set_ylabel("Temperature (F)/Pressure/Humidity/Altitude")


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.show()
