import csv
import random
import time

fieldnames = ["dateTime", "Temperature", "Pressure", "Humidity", "Altitude"]


with open('4c1d96a4f70e_BME20.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

