# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/03_makemore.bigram.ipynb.

# %% auto 0
__all__ = ['stoi', 'itos']

# %% ../../nbs/03_makemore.bigram.ipynb 3
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import torch
import torch.nn.functional as F

# %% ../../nbs/03_makemore.bigram.ipynb 12
def stoi(words, start_str='<S>', end_str='<E>'):
    if start_str != end_str:
        d = {s:i for i,s in enumerate(sorted(list(set("".join(words)))))}
        n = len(d.values())
        d[start_str] = n
        d[end_str] = n+1
    else:
        d = {s:i+1 for i,s in enumerate(sorted(list(set("".join(words)))))}
        d[start_str] = 0
    return d

# %% ../../nbs/03_makemore.bigram.ipynb 13
def itos(stoi):
    return { v:k for k, v in stoi.items()}
