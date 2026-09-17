import torch

exec(open('load_training_data.py').read())
exec(open('nn_optimizer.py').read())

num_epochs = 200
for epoch in range(num_epochs):
    for x_batch, y_batch in train_dl:
        pred = model(x_batch)
        loss = loss_fn(pred, y_batch)
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

    if epoch % 20 == 0:
        print(f'Epoch {epoch:4d}  loss={loss.item():.4f}  weight={weight.item():.4f}  bias={bias.item():.4f}')

print()
print(f'Final: weight={weight.item():.4f}  bias={bias.item():.4f}')
