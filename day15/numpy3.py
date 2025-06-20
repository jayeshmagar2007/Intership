'''Indexing and Slicing
Extract the first 5 elements of an array.

Extract the last 3 elements.

Change every second element of an array.

Extract an element from a 2D array.

Slice a 2D array to get its first 2 rows and first 2 columns.'''
import numpy as np
arr =np.array([15,27,35,54,87,66,99])
print(arr[:5])
print(arr[-3:])

arr[::2]=33
print(arr)

arr2 =np.array([[10,20,30,40],[50,60,70,80]])
print(arr2[1][1])


print(arr2[:2,:2])