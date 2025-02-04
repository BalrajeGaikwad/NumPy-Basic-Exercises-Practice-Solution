# Write a  NumPy program to create a vector with values ​​from 0 to 20 and change the sign of the numbers in the range from 9 to 15.

import numpy as np
x=np.arange(21)

print("original array")
print(x)

#  printing a msg indicating changing the sign of number in the range from 9 to 15
#  using boolean indexing , multiplying elements between 9 to 15 by -1 to change theri sign x[(x >=9) & (x<= 15)] *=-1

x[(x >=9) & (x<= 15)] =-1
print("After changing sign of number in the range from 9 to 15: ")
print(x)