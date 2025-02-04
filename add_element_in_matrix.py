# Write a  NumPy program to add elements to a matrix. If an element in the matrix is 0, we will not add the element below this element.

import numpy as np

def sum_matrix_element(m):
    arr=np.array(m)
    element_sum=0

    #looping throw rows of the array
    for p in range(len(arr)):
        #looping through column array
        for q in range(len(arr[p])):
            if arr[p][q]== 0 and p <len(arr)-1:
                arr[p+1][q]=0
            element_sum+=arr[p][q]
    return element_sum
m=[[1,1,0,2],
   [0,3,0,3],
   [1,0,4,4]]

print("original matrix")
print(m)

print("sum")
print(sum_matrix_element(m))