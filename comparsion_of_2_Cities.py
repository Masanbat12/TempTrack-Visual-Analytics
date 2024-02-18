import csv
import matplotlib.pyplot as plt
from datetime import datetime, date


# Helper function to read and process CSV data using the csv module
def read_csv_data(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        data = {'DATE': [], 'TMAX': [], 'TMIN': []}
        for row in reader:
            data['DATE'].append(datetime.strptime(row['DATE'], '%Y-%m-%d'))  # Adjust the format if necessary
            data['TMAX'].append(float(row['TMAX']) if row['TMAX'] else None)
            data['TMIN'].append(float(row['TMIN']) if row['TMIN'] else None)
    return data


# Replace these with your actual CSV file paths
city1_data = read_csv_data('data/aaa.csv')
city2_data = read_csv_data('data/bbb.csv')

# Plot the data for City 1
plt.figure(figsize=(12, 6))
plt.plot(city1_data['DATE'], city1_data['TMAX'], label='City 1 Max Temp', color='orange', marker='o')
plt.plot(city1_data['DATE'], city1_data['TMIN'], label='City 1 Min Temp', color='blue', marker='o')

# Plot the data for City 2
plt.plot(city2_data['DATE'], city2_data['TMAX'], label='City 2 Max Temp', color='red', linestyle='--', marker='x')
plt.plot(city2_data['DATE'], city2_data['TMIN'], label='City 2 Min Temp', color='green', linestyle='--', marker='x')

# Formatting the plot
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.title('Temperature Comparison Between Two Cities')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()
