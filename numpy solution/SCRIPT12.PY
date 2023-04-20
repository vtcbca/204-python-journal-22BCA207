#script to conert a list into numpy array print original list and numpyarray with its dimention,size and byte occupied in memory.
import numpy as np 

22=[10,23.4,50,345,66]
b1=np.array(22)
print(f"Original list:{22}")

print(f"Numpy array:{b1}")

print(f"Dimention of array is = {b1.ndim}\nsize of array = {b1.size}\nBytes occupied in memory = {b1.size*b1.itemsize}")
