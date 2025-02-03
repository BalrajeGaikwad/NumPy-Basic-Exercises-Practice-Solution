# Test whether none of the elements of a given array is zero

import numpy as np
import pandas as pd

x=np.array([[1,2,3,4]])
print("array of x")
print(x)

print(np.all(x))

y=np.array([[0,1,2,3,4]])
print("array of y")
print(y)

print(np.all(y))