# Write a NumPy program to sort a given array by row and 
# column in ascending order.

import numpy as np

nums=np.array([[4, 3, 7],
              [5, 8, 9],
              [1, 2, 2]])
print("original arrray")
print(nums)

# sorting an array nums by rows in ascending order and displaying the sort
print("\n sort the said array by row in ascending orde :")
row=np.sort(nums)
print(row)

# sorting an array nums by columns in ascending order and displaying the sort
print("\n sort the said array by columns in ascending orde :")
columns=np.sort(row, axis=0)
print(np.sort(row, axis=0))

unique_arr=np.unique(columns)
print(unique_arr.reshape(4,2))
