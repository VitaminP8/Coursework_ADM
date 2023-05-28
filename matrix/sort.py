import numpy as np

def sort_2d_array(array_2d):
    # Преобразование двумерного массива в одномерный массив
    flattened_array = np.ravel(array_2d)

    # Применение сортировки к одномерному массиву
    sorted_array = np.sort(flattened_array)

    # Обратное преобразование отсортированного одномерного массива к двумерному виду
    sorted_2d_array = sorted_array.reshape(array_2d.shape)

    return sorted_2d_array



# arr.sort(axis=1) по строкам
# arr.sort(axis=0) по столбцам

