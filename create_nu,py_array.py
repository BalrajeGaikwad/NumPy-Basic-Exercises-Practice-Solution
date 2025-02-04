# NumPy: Create a 3X4 array using and iterate over it

import numpy as np

a=np.arange(10,22).reshape((3,4))
print("original array ")
print(a)
print("Each Element of the array is :")

for x in np.nditer(a):
    print(x, end=" ")