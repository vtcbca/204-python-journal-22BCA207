#write a numpy script to create a new shape to an array without changing its data.

import numpy as np
p=np.array([1,5,3,5,6,18,22,34,21,25,37,90,44,34])
q=np.reshape(p,(3,4))
r=np.reshape(q,(4,3))

print("Reahape 3x4 :\n",q)

print("Reahape 3x4 :\n",r)
