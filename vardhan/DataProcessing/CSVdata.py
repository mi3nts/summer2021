import pandas as pd
import csv
import math

# ***************************************************************************
#   ---------------------------------
#   Written by: Vardhan Agnihotri
#   - for -
#   Mints: Multi-scale Integrated Sensing and Simulation
#   ---------------------------------
#   Date: July 9th, 2021
#   ---------------------------------
#   This module is written for generic implimentation of MINTS projects
#   ---------------------------------------------------------------------
#   https://github.com/mi3nts
#
#   Contact:
#      email: 24agnihotriv@smtexas.org
# ***********************************************************************
#   Averaging measurements every 60 values (template for Adit)

utdNode = pd.read_csv("C:/Users/usr/PycharmProjects/mintsML/files/mintsUTDData.csv")
EPAdata = pd.read_csv("C:/Users/usr/PycharmProjects/mintsML/files/EPAdata.csv")


measureEPAList = EPAdata.measurement.tolist()
measureNodeList = utdNode.OPCN2_pm2_5.tolist()
measureEPAAvg = []
measureNodeAvg = []

sum = 0

#for EPA list
# for i in range(math.floor(len(measureEPAList)/60) - 1):

#     for j in range(i*60, ((i+1)*60)-1):
#         sum = sum + measureEPAList[j]
#         avg = sum/60

#     measureEPAAvg.append(avg)
#     sum = 0
# print(measureAvg)

#for Node list
for i in range(math.floor(len(measureNodeList)/60) - 1):

    for j in range(i*60, ((i+1)*60)-1):
        sum = sum + measureNodeList[j]
        avg = sum/60

    measureNodeAvg.append(avg)
    sum = 0
print(measureNodeAvg)
