#Write a NumPy program to get the values and indices of the elements that are bigger than 10 in a given array.


import numpy as np
b = np.array([[20,3,4,90,60,7]])
print("Value that are big than 10 and it's indecs:")
print("indecies:",np.where((b>10)[0]))
print("vaules:",b[b>10])
