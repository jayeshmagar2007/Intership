'''Random Numbers
Create an array of 5 random numbers between 1–100.

Create a 3x3 array with random floats between 0–1.

Create a 4x4 array of random integers between 10–50.'''
import numpy as np

arr=np.random.randint(1,100,size =5)
print(arr)

arr1 = np.random.rand(3,3)
print(arr1)

arr2 =np.random.randint(10,50,[4,4])
print(arr2)