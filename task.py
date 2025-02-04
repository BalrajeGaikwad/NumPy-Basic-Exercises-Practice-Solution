import numpy as np

a=np.arange(1,11).reshape(5,2)
print("First array")
print(a)

b=np.arange(1,11).reshape(5,2)
print("Second Array")
print(b)

first_array_selected = np.array([
    [a[0, 0], a[0, 1]],  # (1,2)
    [a[1, 0], a[1, 1]],  # (5,6)
    [a[2, 0], a[3, 0]],
    [a[3, 1], a[4, 0]],
    [a[3, 1], a[4, 0]]   # (9,10)
])
print(first_array_selected)
# Extracting required elements from the second array
second_array_selected = np.array([
    [b[0, 1], b[1, 0]],  # (2,3)
    [b[1, 1], b[2, 0]],  # (5,6)
    [b[2, 1], b[3, 0]],  # (7,8)
    [b[3, 1], b[4, 0]],
    [b[3, 1], b[4, 0]]   # (9,10)
])
print(second_array_selected)

combined_array = np.vstack((first_array_selected, second_array_selected))

print("combined array ")
print(combined_array)

"""# Using numpy's unique function to remove duplicates while keeping order
_, unique_indices = np.unique(combined_array, axis=0, return_index=True)
final_array = combined_array[np.sort(unique_indices)]

# Printing the final combined 2D array
print("Final Combined 2D Array (Unique & Sorted):")
print(final_array)"""