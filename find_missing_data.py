# Write a NumPy program to find missing data in a given array.



import numpy as np

nums=np.array([[3,2,np.nan,1],
               [10,12,10,9],
               [5,np.nan, 1, np.nan]])

print("original Array")

print(nums)

print(np.isnan(nums))