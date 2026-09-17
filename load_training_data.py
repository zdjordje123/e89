import csv
import numpy as np
import torch

celsius, fahrenheit = [], []
with open('temperature_measurements.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        celsius.append(float(row['temperature_celsius']))
        fahrenheit.append(float(row['temperature_fahrenheit']))

X_train = np.array(celsius)
y_train = np.array(fahrenheit)

celsius_mean = X_train.mean()
celsius_std = X_train.std()

X_train_norm = torch.tensor((X_train - celsius_mean) / celsius_std, dtype=torch.float32)
y_train = torch.tensor(y_train, dtype=torch.float32)
