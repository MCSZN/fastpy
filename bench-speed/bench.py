from ctypes import cdll
from numba import njit, vectorize, float64
from time import time
from ctypes import *
from typing import *
import numpy as np
import math

import cProfile


'''
C operations
'''

# importing the C library
nn = cdll.LoadLibrary('C/main.so')

# ctypes assumes C libs return ints
# you need to change that for each function
nn.relu.restype = c_float
nn.activation.restype = c_double
nn.sigmoid.restype = c_double
nn.neuron.restype = c_double

# ctypes does not accept python native
# float objects, it needs conversion
LENTH = 1000

array = c_double * LENTH
X = array()
W = array()
B = array()
for i in range(LENTH):
	X[i] = np.random.rand(1)[0]
	W[i] = np.random.rand(1)[0]
	B[i] = np.random.rand(1)[0]


def looping(iterations: int) -> None:
	for i in range(iterations):
		nn.relu(c_float(i))
		nn.activation(c_double(i))
		nn.sigmoid(c_double(i))
		nn.neuron(c_int(LENTH), X, W, B)


cProfile.run('looping(100000)')

start = time()
looping(1000000)
end = time()
print('C Operations took: {}'.format(end-start))

'''
Numpy Numba operations
'''
nums = np.random.rand(1000)


@vectorize([float64(float64)])
def relu(x):
	if x > 0:
		return x
	else:
		return 0

@vectorize([float64(float64)])
def activation(x):
	return np.tanh(x)

@vectorize([float64(float64)])
def sigmoid(x):
	out = 1/(1+np.exp(-x))
	return out

@njit()
def neuron(X, W, B):
	out  = np.tanh(np.sum(np.add(np.multiply(X,W),B)))
	return out

@njit(parallel=True)
def looping(iterations):
	for i in range(iterations):
		relu(i)
		activation(i)
		sigmoid(i)
		neuron(nums,nums,nums)

start = time()
looping(1000000)
end = time()
print('Numba Numpy Operations took: {}'.format(end-start))


'''
Python operations
'''
nums = list(range(1000))

def relu(x: int) -> int:
	if x > 0:
		return x
	else:
		return 0

def activation(x: float) -> float:
	return math.tanh(x)

def sigmoid(x: float) -> float:
	out = 1/(1+math.exp(-x))
	return out

def neuron(X: List, W: List, B: List) -> int:
	return math.tanh(sum([(x*w)+b for x,w,b in zip(X,W,B)]))

def looping(iterations: int) -> None:
	for i in range(iterations):
		relu(i)
		activation(i)
		sigmoid(i)
		neuron(nums, nums, nums)

USE_PYTHON = False

if USE_PYTHON:
	start = time()
	looping(1000000)
	end = time()
	print('Pure Python Operations took: {}'.format(end-start))
else:
	print('Pure Python is too slow to benchmark')

'''
Results // 
	=> if need to use C or any compiled so use ctypes
	=> if need speed use numba.jit, numba.vectorize with numpy
'''

