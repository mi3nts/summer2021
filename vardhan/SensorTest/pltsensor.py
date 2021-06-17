import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
from pyqtgraph import AxisItem
import numpy as np
import pandas as pd
import time
from datetime import datetime, timedelta
from mintsXU4 import mintslatest as mL
from getmac import get_mac_address as gma

macaddr = gma()
mac_name = macaddr.replace(":", "")
mac_topicname = macaddr.replace(":", "")
weathersensor_id = "BME20"
rainsensor_id = "GCCG41"

class TimeAxisItem(pg.AxisItem):
    def tickStrings(self, values, scale, spacing):
        return [datetime.fromtimestamp(value) for value in values]

class Graph():
    def __init__(self, ):
        self.win = pg.GraphicsLayoutWidget( title="SensorTest")
        self.app = QtGui.Application([])
        self.lookBack = timedelta(minutes=1)
        graphUpdateSpeedMS = 100

        #Initialize weathersensor mock data
        self.initRun_weather = True

        self.dateTime_weather = []
        self.temperature_weather = []
        self.pressure_weather = []
        self.humidity_weather = []
        self.altitude_weather = []

        #Plot weathersensor mock data
        self.p1_weather = self.win.addPlot(axisItems = {"bottom": TimeAxisItem(orientation="bottom")}, title="weathersensor mock data")
        self.curveTemperature_weather = self.p1_weather.plot()
        self.curvePressure_weather = self.p1_weather.plot()
        self.curveHumidity_weather = self.p1_weather.plot()
        self.curveAltitude_weather = self.p1_weather.plot()

        self.p1_weather.showGrid(x=True, y=True)
        self.p1_weather.setLabels(
            left="measurements",
            bottom="dateTime"
        )

        self.legend_weather=pg.LegendItem(offset={0., .5})
        self.legend_weather.setParentItem(self.p1_weather.graphicsItem())
        self.legend_weather.addItem(self.curveTemperature_weather, "Temperature")
        self.legend_weather.addItem(self.curvePressure_weather, "Pressure")
        self.legend_weather.addItem(self.curveHumidity_weather, "Humidity")
        self.legend_weather.addItem(self.curveAltitide_weather, "Altitude")

        timer = QtCore.Qtimer()
        timer.timeout.connect(self.update)
        timer.start(graphUpdateSpeedMS)
        QtGui.QApplication.instance().exec_()

    def recursiveWeather(self):
        if self.dateTime_frog[0] < self.currentTime - self.lookBack:
            self.temperature_weather.pop(0)
            self.pressure_weather.pop(0)
            self.humidity_weather.pop(0)
            self.altitude_weather.pop(0)
            if len(self.dateTime_weather) == 0:
                self.initRun_weather = True
            else:
                self.recursivePoper_frog()
        else:
            return

    def weatherUpdater(self):
        self.dateTime_weather.append(self.ctNow_weather)
        self.temperature_weather.append(self.temperatureNow_weather)
        self.pressure_weather.append(self.pressureNow_weather)
        self.humidity_weather.append(self.humidityNow_weather)
        self.altitude_weather.append(self.altitudeNow_weather)

        self.curveTemperature_weather.setData(x=[x.timestamp() for x in self.dateTime_weather],\
                        y=self.pm2_5_frog,pen=pg.mkPen('g', width=1,name = "Temperature"))
        self.curvePressure_weather.setData(x=[x.timestamp() for x in self.dateTime_weather], \
                        y=self.pm4_frog,pen=pg.mkPen('b', width=1,name="Pressure"))
        self.curveHumdiity_weather.setData(x=[x.timestamp() for x in self.dateTime_weather], \
                        y=self.pm10_frog,pen=pg.mkPen('r', width=1,name = "Humidity"))
        self.curveAltitude_weather.setData(x=[x.timestamp() for x in self.dateTime_weather],\
                        y=self.pm1_frog,pen=pg.mkPen('w', width=1,name="Altitude"))

    def weatherReader(self):
        dataIn = mL.readJSONLatestAllMQTT()[0]

        self.temperatureNow_weather = float(dataIn["Temperature"])
        self.pressureNow_weather = float(dataIn["Pressure"])
        self.humidityNow_weather = float(dataIn["Humidity"])
        self.altitudeNow_weather = float(dataIn["Altitude"])
        self.ctNow_weather = datetime.strptime(dataIn['dateTime'], '%Y-%m-%d %H:%M:%S').replace(
            tzinfo=tz.tzutc()).astimezone(tz.gettz())

        if self.initRun_weather:
            if (self.temperature_weather>0.00):
                    self.initRun_licor = False
                    self.licorUpdater()
        else:
            if (self.temperature_weather>0.00 and self.ctNow_weather>=self.dateTime_weather[-1] ):
                    self.recursiveWeather()
                    self.weatherUpdater()

    def update(self):
        self.currentTime = datetime.now().astimezone(tz.gettz())
        self.weatherReader()
        self.app.processEvents()

if __name__ == "main":
    Graph()
