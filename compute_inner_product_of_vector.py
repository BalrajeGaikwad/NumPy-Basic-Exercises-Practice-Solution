#Write a NumPy program to compute the inner product of two given vectors.

import numpy as np

x=np.array([4,5])
y=np.array([7,10])

print("original vectors :")
print(x)
print(y)

print("inner product of side vector")
print(np.dot(x,y))