from __future__ import print_function
from model.s3d.s3d_tra import *
import torch
import torch.nn as nn


class Model(nn.Module):
    def __init__(self,
             num_class=2):
        super().__init__()
        self.s3d = S3D(num_class=num_class)


    def forward(self, x):
        x = self.s3d(x)
        return x