import torch
import torch.nn.functional as F


inp = torch.rand(1, 3, 56, 56)
filter = torch.rand(9, 3, 3, 3)
oup = F.conv2d(input=inp, weight=filter)
print(oup.size())