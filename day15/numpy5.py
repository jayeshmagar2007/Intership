'''Math Operations
Perform element-wise addition, subtraction, multiplication, and division between two arrays.

Perform power and square root operations.

Use np.sum(), np.mean(), np.min(), np.max(), and np.std().'''
import numpy as np

arr= np.array([10,20,30,40,50,60])
arr1 = np.array([1,2,3,4,5,6])
print(arr+arr1)
print(arr-arr1)
print(arr*arr1)
print(arr/arr1)
print(np.power(arr1,3))
print(np.square(arr))
print(np.square(arr1))

arr2=np.array([10,20,30,40,50])
print(np.sum(arr2))
print(np.mean(arr2))
print(np.max(arr2))
print(np.min(arr2))
print(np.std(arr2))