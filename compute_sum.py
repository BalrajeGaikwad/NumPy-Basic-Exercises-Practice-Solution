# Write a NumPy program to compute the sum of all elements, 
# the sum of each column and the sum of each row in a given array.

import numpy as np

x=np.array([[1,2],[3,2]])
print(x)

print("sum of all elements :")
print(np.sum(x))

print("sum of column")
print(np.sum(x, axis=0))

print("sum of row")
print(np.sum(x, axis=1))

