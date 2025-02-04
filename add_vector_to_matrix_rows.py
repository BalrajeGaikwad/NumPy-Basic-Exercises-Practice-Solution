# Write a NumPy program to compute the inner product of two given vectors.

import numpy as np

m=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])

v=np.array([1,1,0])                   #--- vector

print("original matrix")
print(m)

print("original vector ")
print(v)

#creating empty matrix 
result=np.empty_like(m)

for i in range(4):
    result[i, :]=m[i, :]+v

print("Ater adding the vector v to matrix m ")
print(result)