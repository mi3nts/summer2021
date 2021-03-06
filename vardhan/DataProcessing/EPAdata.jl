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
% #   DataFrames concatenation + EPA data analysis w/ modifiable function

function getDataFrame(bdate, edate, param, state, county, site)
    url = "https://aqs.epa.gov/data/api/sampleData/bySite?email=va648314@gmail.com&key=bayhare31&param=$param&bdate=$bdate&edate=$edate&state=$state&county=$county&site=$site"
    resp = HTTP.get(url)
    str = String(resp.body)
    jobj = JSON.parse(str)

    dateTimeList = []
    latList = []
    longList = []
    measureEPAList = []


    dfUTD = DataFrame(CSV.File("C:/Users/usr/PycharmProjects/mintsML/files/UTD2_5Data.csv"))
    measureUTDList = dfUTD.OPCN2_pm2_5

    for i in 1:length(jobj["Data"])
        dateStr = jobj["Data"][i]["date_local"]
        time = jobj["Data"][i]["time_local"]
        latitude = jobj["Data"][i]["latitude"]
        longitude = jobj["Data"][i]["longitude"]
        measurement = jobj["Data"][i]["sample_measurement"]

    dateTime = dateStr * " " * time

        if measurement == nothing
            continue
        else
            push!(dateTimeList, dateTime)
            push!(latList, latitude)
            push!(longList, longitude)
            push!(measureEPAList, measurement)
        end
    end

    reverseDateTime = reverse(dateTimeList)
    reverseLat = reverse(latList)
    reverseLong = reverse(longList)
    reverseEPAMeasure = reverse(measureEPAList)
    reverseUTDMeasure = reverse(measureUTDList)

    df = DataFrame(dateTime = reverseDateTime, latitude = reverseLat, longitude = reverseLong, measurementEPA = reverseEPAMeasure)
    println(df)
    # CSV.write("files/EPAdata.csv", df)

end

getDataFrame(20200101, 20201231, 88101, 48, 439, 1006)
