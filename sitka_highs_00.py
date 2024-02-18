import csv

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)
#  After running the loop, the output:
#     ['STATION', 'NAME', 'DATE', 'PRCP', 'TAVG', 'TMAX', 'TMIN']

    """ enumerate() returns both the index of each item and the
        value of each item as you loop through a list """
    for index, column_header in enumerate(header_row):
        print(index, column_header)
# output:
# 0 STATION
# 1 NAME
# 2 DATE
# 3 PRCP
# 4 TAVG
# 5 TMAX
# 6 TMIN

# Get high temperatures from this file.
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)

print(highs)
# output:
# [62, 58, 70, 70, 67, 59, 58, 62, 66, 59, 56, 63, 65, 58, 56, 59,
# 64, 60, 60, 61, 65, 65, 63, 59, 64, 65, 68, 66, 64, 67, 65]


