import numpy as np
from matrix.sort import sort_2d_array

matrix3 = np.random.randint(0, 1000, size=(3, 3))
matrix5 = np.random.randint(0, 1000, size=(5, 5))
matrix10 = np.random.randint(0, 1000, size=(10, 10))
matrix20 = np.random.randint(0, 1000, size=(20, 20))
matrix40 = np.random.randint(0, 1000, size=(40, 40))


print(matrix5)
print("****")
print(sort_2d_array(matrix5))
x = matrix5[3][3]
print()