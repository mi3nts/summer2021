using HTTP, JSON
using MAT
using CSV
using DataFrames
import Dates

% # ***************************************************************************
% #   ---------------------------------
% #   Written by: Vardhan Agnihotri
% #   - for -
% #   Mints: Multi-scale Integrated Sensing and Simulation
% #   ---------------------------------
% #   Date: July 8th, 2021
% #   ---------------------------------
% #   This module is written for generic implimentation of MINTS projects
% #   ---------------------------------------------------------------------
% #   https://github.com/mi3nts
% #
% #   Contact:
% #      email: 24agnihotriv@smtexas.org
% # ***********************************************************************
% #   DataFrames concatenation



resp = HTTP.get("https://aqs.epa.gov/data/api/sampleData/bySite?email=va648314@gmail.com&key=bayhare31&param=88101&bdate=20200101&edate=20201231&state=48&county=439&site=1006")
str = String(resp.body)
jobj = JSON.parse(str)

dateTimeList = []
latList = []
longList = []
measureList = []


for i in 1:length(jobj["Data"])
    dateStr = jobj["Data"][i]["date_local"]
    time = jobj["Data"][i]["time_local"]
    latitude = jobj["Data"][i]["latitude"]
    longitude = jobj["Data"][i]["longitude"]
    measurement = jobj["Data"][i]["sample_measurement"]

    dateSplit = split(dateStr, "-")
    timeSplit = time[1:2]

    dateCompile = dateSplit[1] * dateSplit[2] * dateSplit[3]
    timeCompile = timeSplit * "0000"

    dateTime = dateCompile * " " * timeCompile


    df = Dates.DateTime(dateTime, "yyyymmdd HHMMSS")

#     year = parse(Int64, dateStr[1:4])
#     month = parse(Int64, dateStr[6:7])
#     date = parse(Int64, dateStr[9:10])
#
#     dateDateType = Dates.Date(year, month, date)

    if measurement == nothing
        continue
    else
        push!(dateTimeList, df)
        push!(latList, latitude)
        push!(longList, longitude)
        push!(measureList, measurement)
    end
end

reverseDateTime = reverse(dateTimeList)
reverseLat = reverse(latList)
reverseLong = reverse(longList)
reverseMeasure = reverse(measureList)

df = DataFrame(dateTime = reverseDateTime, latitude = reverseLat, longitude = reverseLong, measurement = reverseMeasure )
println(df)
CSV.write("files/EPAdata.csv", df)
