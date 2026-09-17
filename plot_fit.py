import numpy as np
import torch
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

exec(open('load_training_data.py').read())
exec(open('linear_model.py').read())

loss_fn = torch.nn.MSELoss()
optimizer = torch.optim.SGD([weight, bias], lr=0.1)

num_epochs = 200
for epoch in range(num_epochs):
    for x_batch, y_batch in train_dl:
        pred = model(x_batch)
        loss = loss_fn(pred, y_batch)
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

celsius_range = np.linspace(X_train.min() - 2, X_train.max() + 2, 100)
celsius_range_norm = (celsius_range - celsius_mean) / celsius_std
with torch.no_grad():
    fahrenheit_fit = model(torch.tensor(celsius_range_norm, dtype=torch.float32)).numpy()

fig, ax = plt.subplots(figsize=(8, 6))

ax.scatter(X_train, y_train.numpy(), color='#d55e00', s=70, zorder=3, label='Experimental points')
ax.plot(celsius_range, fahrenheit_fit, color='#009e73', linewidth=2, zorder=2,
        label=f'Fitted line (w={weight.item():.2f}, b={bias.item():.2f})')

ax.set_xlabel('Temperature (°C)')
ax.set_ylabel('Temperature (°F)')
ax.set_title('Linear Regression Fit: Celsius vs Fahrenheit')
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend()

fig.tight_layout()
fig.savefig('temperature_fit.png', dpi=150)
print('saved temperature_fit.png')
