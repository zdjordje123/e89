import torch
import torch.nn as nn

exec(open('linear_model.py').read())

loss_fn = nn.MSELoss()
optimizer = torch.optim.SGD([weight, bias], lr=0.1)
