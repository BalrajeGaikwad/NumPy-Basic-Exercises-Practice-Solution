# Create an element-wise comparison (equal, equal within a tolerance) of two given arrays

import numpy as np

x=np.array([72, 79, 85, 90, 150, -135, 120, -10, 60, 100])
y=np.array([72, 79, 85, 90, 150, -135, 120, -10, 60, 100.000001])

print("original numbers ")
print(x)
print(y)

print("Comparsion - equal : ")
print(np.equal(x,y))

# Checking if arrays 'x' and 'y' are element-wise equal within a tolerance, and printing the result
print("Comparison - equal within a tolerance:")
print(np.allclose(x, y)) 