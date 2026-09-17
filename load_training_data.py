import csv
import numpy as np

celsius, fahrenheit = [], []
with open('temperature_measurements.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        celsius.append(float(row['temperature_celsius']))
        fahrenheit.append(float(row['temperature_fahrenheit']))

X_train = np.array(celsius)
y_train = np.array(fahrenheit)
