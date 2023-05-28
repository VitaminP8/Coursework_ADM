import math


def exponential_search(arr, target):
    n = len(arr)

    if arr[0] == target:
        return 0

    # Находим диапазон, в котором может находиться искомый элемент
    i = 1
    while i < n and arr[i] <= target:
        i *= 2

    # Применяем бинарный поиск в найденном диапазоне
    left = i // 2
    right = min(i, n - 1)
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1



def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1

        # Интерполяционная формула для нахождения позиции
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1  # Значение не найдено




def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1

        # Интерполяционная формула для нахождения позиции
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1  # Значение не найдено




def block_search(arr, target, block_size):
    n = len(arr)
    num_blocks = n // block_size

    # Поиск блока, в котором может находиться искомый элемент
    block_index = 0
    while block_index < num_blocks and arr[block_index * block_size] <= target:
        block_index += 1

    # Если блок с индексом block_index содержит искомый элемент, выполняем линейный поиск в этом блоке
    if arr[(block_index - 1) * block_size] == target:
        return (block_index - 1) * block_size

    # Выполняем бинарный поиск в предыдущем блоке
    left = (block_index - 1) * block_size
    right = min(block_index * block_size - 1, n - 1)
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1




def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    # Поиск блока, в котором может находиться искомый элемент
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    # Выполняем линейный поиск в найденном блоке
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1

    if arr[prev] == target:
        return prev
    return -1





def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return mid

    return -1




def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
