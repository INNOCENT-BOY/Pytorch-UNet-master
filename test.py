import torch.nn.functional as F
import torch

a = torch.rand(1, 3, 120, 120)
b = torch.ones(1, 1, 120, 120, dtype=torch.int64)

loss = F.cross_entropy(a, b).item()

print(loss)