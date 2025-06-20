'''Inspecting Arrays

Create a sample array of float64

Find the shape, size, and dtype of an array.

Change the dtype of an array from float64 to int32.

Find the number of dimensions (ndim) of an array.'''
import numpy as np
arr= np.array([10.10,11.20,14.30,40.40,54.50],dtype=np.float64)
print(arr)

shape=np.shape(arr)
print(shape)

size =np.size(arr)
print(size)

datatype= np.int32(arr)
print(datatype)

dimen= np.ndim(arr)
print(dimen)