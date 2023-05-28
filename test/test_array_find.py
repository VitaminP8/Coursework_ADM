import math
import numpy as np
from arrays.find import (linear_search, binary_search,
                         jump_search, block_search,
                         interpolation_search, exponential_search)

arr50 = np.random.randint(0, 1000, size=50)
arr500 = np.random.randint(0, 1000, size=500)
arr5000 = np.random.randint(0, 1000, size=5000)
arr50000 = np.random.randint(0, 1000, size=50000)
arr500000 = np.random.randint(0, 1000, size=500000)
arr1000000 = np.random.randint(0, 1000, size=1000000)

arr50.sort()
print(arr50)
x = arr50[28]
print(x)

print(linear_search(arr50, x))
print(binary_search(arr50, x))
print(jump_search(arr50, x))
print(block_search(arr50, x, 10))
print(interpolation_search(arr50, x))
print(exponential_search(arr50, x))