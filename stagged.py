# Write a NumPy program to create a 4x4 matrix in which 0 and 1 are staggered, with zeros on the main diagonal.

import numpy as np

a=np.zeros((4,4))
print(a)

a[::2 , 1::2]=1

a[1::2, ::2]=1

print(a)