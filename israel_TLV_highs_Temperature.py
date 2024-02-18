import csv
from datetime import datetime, date
import matplotlib.pyplot as plt
import pandas as pd

filename = 'data/israel_TLV_01-02-24_to_14-02-24_temperature.csv'
# Read the CSV data into a pandas DataFrame
with open(filename, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    dates, tavg, tmax, tmin = [], [], [], []

    for row in csvreader:
        # Parse the DATE column into a datetime object
        date = datetime.strptime(row['DATE'], '%Y-%m-%d')
        dates.append(date)

        # Try to convert TAVG, TMAX, TMIN to float, if not possible use NaN to denote missing data
        tavg.append(float(row['TAVG']) if row['TAVG'] else float('nan'))
        tmax.append(float(row['TMAX']) if row['TMAX'] else float('nan'))
        tmin.append(float(row['TMIN']) if row['TMIN'] else float('nan'))

# Create a pandas DataFrame from the lists
df = pd.DataFrame({
    'DATE': dates,
    'TAVG': tavg,
    'TMAX': tmax,
    'TMIN': tmin
})

# Handle missing data, forward fill in this example
df['TMAX'].fillna(method='ffill', inplace=True)
df['TMIN'].fillna(method='ffill', inplace=True)

# Plot the data
plt.figure(figsize=(15, 5))
plt.plot(df['DATE'], df['TAVG'], label='Average Temperature (TAVG)', marker='o')
plt.plot(df['DATE'], df['TMAX'], label='Max Temperature (TMAX)', marker='o')
plt.plot(df['DATE'], df['TMIN'], label='Min Temperature (TMIN)', marker='o')

plt.xlabel('Date')
plt.ylabel('Temperature')
plt.title('Daily Temperatures of 13 days in TLV, Israel')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

