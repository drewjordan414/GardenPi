import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import torch
from torchvision import datasets, transforms, models  # datsets  , transforms
from torch.utils.data.sampler import SubsetRandomSampler
import torch.nn as nn
import torch.nn.functional as F
from datetime import datetime

# %load_exit nb_black ----> black formatter matlab

transform = transforms.Compose(
    [transforms.Resize(255), transforms.CenterCrop(224), transforms.ToTensor()]
)

dataset = datasets.ImageFolder("data", transform=transform) # -----> load the dataset for the model 

# split the dataset into training and validation sets
valid_size = 0.2
num_train = len(dataset)
indices = list(range(num_train))
np.random.shuffle(indices)
split = int(np.floor(valid_size * num_train))
train_idx, valid_idx = indices[split:], indices[:split]
validation = SubsetRandomSampler(valid_idx)
train = SubsetRandomSampler(train_idx)

# define samplers for obtaining training and validation batches
print(0, validation , split, train_idx, valid_idx, len(train_idx), len(valid_idx))
train_loader = torch.utils.data.DataLoader(
    dataset, batch_size=20, sampler=train, num_workers=0
)


