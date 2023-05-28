import numpy as np


def binary_search_2d(array_2d, target):
    rows, cols = array_2d.shape

    for row in range(rows):
        sorted_row = np.sort(array_2d[row])
        found_index = np.searchsorted(sorted_row, target)
        if found_index < cols and sorted_row[found_index] == target:
            col = np.where(array_2d[row] == target)[0][0]
            return (row, col)

    return -1



# np.where



def linear_search_2d(array_2d, target):
    indices = np.where(array_2d == target)
    if len(indices[0]) > 0:
        return list(zip(indices[0], indices[1]))
    else:
        return -1