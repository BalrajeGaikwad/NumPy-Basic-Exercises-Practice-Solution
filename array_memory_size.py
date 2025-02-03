# Write a  NumPy program to create an array with the values 1, 7, 13, 105 and determine the size of the memory occupied by the array.

import numpy as np
x=np.array([1,7,13,105])

print("original array")
print(x)

print("Size of the memory occupied by the said array:")
print("%d bytes" % (x.size * x.itemsize)) 


array = np.arange(30, 71)
print(array)

array1 = np.arange(30, 71, 2)
print(array1)