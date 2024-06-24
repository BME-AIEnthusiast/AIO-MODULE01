# Examples 1
import torch
import torch.nn as nn


class Softmax(nn.Module):
    def __init__(self):
        super(Softmax, self).__init__()

    def forward(self, x):
        e_x = torch.exp(x - torch.max(x))
        return e_x / e_x.sum(dim=0)


data = torch.Tensor([1, 2, 3])
softmax = Softmax()
output = softmax(data)
print(output)


class SoftmaxStable(nn.Module):
    def __init__(self):
        super(SoftmaxStable, self).__init__()

    def forward(self, x):
        x_max = torch.max(x)
        e_x = torch.exp(x - x_max)
        return e_x / e_x.sum(dim=0)


data = torch.Tensor([1, 2, 3])
softmax_stable = SoftmaxStable()
output = softmax_stable(data)
print(output)
