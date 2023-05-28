def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Находим наибольший элемент среди корня и его потомков
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Если наибольший элемент не является корнем, меняем их местами
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Применяем heapify для затронутого поддерева
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Строим max-кучу, начиная с последнего элемента и двигаясь вверх
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Извлекаем элементы по одному из кучи и помещаем их в конец массива
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        # Восстанавливаем свойство кучи для уменьшенной кучи
        heapify(arr, i, 0)




def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Разделение массива на две половины
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Рекурсивный вызов сортировки для каждой половины
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Объединение двух отсортированных половин
    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Слияние двух половин в отсортированный массив
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Добавление оставшихся элементов из левой половины
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    # Добавление оставшихся элементов из правой половины
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged




def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Выбор опорного элемента
    smaller_elements = []
    equal_elements = []
    larger_elements = []

    for num in arr:
        if num < pivot:
            smaller_elements.append(num)
        elif num == pivot:
            equal_elements.append(num)
        else:
            larger_elements.append(num)

    return quick_sort(smaller_elements) + equal_elements + quick_sort(larger_elements)




def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr




def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr




def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
