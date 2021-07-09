using CSV
using DataFrames


df = DataFrame(CSV.File("files/mintsUTDData.csv"))
print(typeof(df.dateTime[1]))
