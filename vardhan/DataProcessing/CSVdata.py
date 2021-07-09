import pandas as pd
import csv

utdNode = pd.read_csv("C:/Users/va648/PycharmProjects/mintsML/files/mintsUTDData.csv")
EPAdata = pd.read_csv("C:/Users/va648/PycharmProjects/mintsML/files/EPAdata.csv")
print(type(utdNode.dateTime[0]))
print(type(EPAdata.dateTime[0]))