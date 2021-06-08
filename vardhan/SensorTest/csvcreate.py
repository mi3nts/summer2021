import csv
from getmac import get_mac_address as gma
import random
import time

macaddr = gma()
mac_csv = macaddr.replace(":", "")

fieldnames = ["dateTime", "Temperature", "Pressure", "Humidity", "Altitude"]

with open(f'{mac_csv}_BME20.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()
