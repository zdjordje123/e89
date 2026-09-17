import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

celsius, fahrenheit = [], []
with open('temperature_measurements.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        celsius.append(float(row['temperature_celsius']))
        fahrenheit.append(float(row['temperature_fahrenheit']))

fig, ax = plt.subplots(figsize=(8, 6))

ax.scatter(celsius, fahrenheit, color='#d55e00', s=70, zorder=3, label='Measured (randomized °F)')

c_line = [min(celsius) - 2, max(celsius) + 2]
f_line = [c * 9 / 5 + 32 for c in c_line]
ax.plot(c_line, f_line, color='#0072b2', linestyle='--', linewidth=1.5, zorder=2,
        label='Exact conversion (F = C × 9/5 + 32)')

ax.set_xlabel('Temperature (°C)')
ax.set_ylabel('Temperature (°F)')
ax.set_title('Celsius vs Fahrenheit Measurements')
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend()

fig.tight_layout()
fig.savefig('temperature_celsius_vs_fahrenheit.png', dpi=150)
