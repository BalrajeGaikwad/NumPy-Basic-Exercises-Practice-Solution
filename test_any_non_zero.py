# Write a NumPy program to test if any of the elements of a given array are non-zero. 

import numpy as np
x=np.array([1,0,0,0])
print("original array")
print(x)
print("Test whether any of the elements of a given array is non-zero:")
print(np.all(x))

## Reassigning array 'x' to a new array containing all elements as zero

x = np.array([0, 0, 0, 0])

# Printing the new array 'x'
print("Original array:")
print(x)

print("Test whether any of the elements of a given array is non-zero:")
print(np.any(x)) 