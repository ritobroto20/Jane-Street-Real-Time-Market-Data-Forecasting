import pandas as pd
import polars as pl
import numpy as np
import matplotlib.pyplot as plt
import os, gc

import torch
import torch.nn as nn
import torch.nn.functional as F

class yollow:
    def __init__(self):
        self.x = 3
        pass

# a = torch.FloatTensor(4)
# print(a)
# var = 5
y_instance = pd.DataFrame(np.array([[1,2,3,5,71],[6,8,3,10,1]]).T,columns=["col1","col2"])
print(y_instance)
print(isinstance(y_instance,pd.DataFrame))