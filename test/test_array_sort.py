import numpy as np
from arrays.sort import (bubble_sort, insertion_sort, selection_sort,
                         quick_sort, merge_sort, merge, heap_sort, heapify)


arr50 = np.random.randint(0, 1000, size=50)
arr500 = np.random.randint(0, 1000, size=500)
arr5000 = np.random.randint(0, 1000, size=5000)
arr50000 = np.random.randint(0, 1000, size=50000)
arr500000 = np.random.randint(0, 1000, size=500000)
arr1000000 = np.random.randint(0, 1000, size=1000000)

print(arr1000000)
heap_sort(arr1000000)
print(arr1000000)
arr1000000.sort()
print(arr1000000)



