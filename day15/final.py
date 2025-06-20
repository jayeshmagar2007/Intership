import numpy as np
arr= np.random.randint(1,100,(5,5))
print(arr)

print(np.min(arr))
print(np.max(arr))
print(np.mean(arr))
print(np.sum(arr))
arr[arr>50]=-1
print(arr)
np.save("array.npy",arr)