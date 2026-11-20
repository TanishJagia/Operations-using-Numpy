
import numpy as np

# 1. Create an array with elements from 0 to 9
arr = np.arange(10)
print("Original Array:")
print(arr)

# 2. Replace all odd numbers with -1 without modifying the original array
new_arr = np.where(arr % 2 != 0, -1, arr)
print("\nArray after replacing odd numbers with -1:")
print(new_arr)

# 3. Convert the original 1D array into a 2D array with two rows
two_d_arr = arr.reshape(2, 5)
print("\n2D Array with two rows:")
print(two_d_arr)
