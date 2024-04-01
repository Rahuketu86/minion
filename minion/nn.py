# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/02_nn.ipynb.

# %% auto 0
__all__ = ['Module', 'Neuron', 'Layer', 'MLP']

# %% ../nbs/02_nn.ipynb 3
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import math
from .core import Value
import random
from typing import List

# %% ../nbs/02_nn.ipynb 6
class Module(object):
    def __init__(self) -> None:
        pass

    def num_params(self):
        return len(self.parameters())
    
    def parameters(self):
        pass
    # def __repr__(self) -> str:
    #     return "This is a minion module"

# %% ../nbs/02_nn.ipynb 10
class Neuron(Module):
    def __init__(self, nin) -> None:
        super().__init__()
        self.weights = [Value(random.random()) for _ in range(nin)]
        self.bias = Value(random.random())

    def __call__(self, xs) -> Value:
        out = sum((w*x for w,x in zip(self.weights, xs)), self.bias)
        return out.tanh()
    
    def parameters(self):
        return self.weights + [self.bias]


# %% ../nbs/02_nn.ipynb 15
class Layer(Module):

    def __init__(self, nin, nout) -> None:
        super().__init__()
        self.neurons = [Neuron(nin) for _ in range(nout)]

    def __call__(self, xs) -> List[Value]:
        ys = [neuron(xs) for neuron in self.neurons]
        return ys
    
    def parameters(self):
        return [p for neuron in self.neurons for p in neuron.parameters()]


# %% ../nbs/02_nn.ipynb 19
class MLP(Module):
    def __init__(self, nin, nouts) -> None:
        super().__init__()
        self.layers = [Layer(lin, lout) for lin,lout in zip([nin]+nouts[:-1], nouts)]

    def __call__(self, xs):
        x = xs
        for layer in self.layers:
            x = layer(x)
        return x[0] if len(x) ==1 else x
    
    def parameters(self):
        return [p for layer in self.layers for p in layer.parameters()]
