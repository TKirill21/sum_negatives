# sum_negatives
def sum_negative_between_extremes(arr):
    if not arr:
        return 0  # Возвращаем 0 для пустого массива

    max_index = arr.index(max(arr))
    min_index = arr.index(min(arr))

    # Обменяем max_index и min_index, если max_index больше min_index
    if max_index > min_index:
        max_index, min_index = min_index, max_index

    # Сумма отрицательных элементов между max и min
    negative_sum = sum(x for x in arr[max_index + 1:min_index] if x < 0)

    return negative_sum

# Пример использования
A = [-1, 2, -3, 4, -5, 6, -7, 8]
result = sum_negative_between_extremes(A)
print("Сумма отрицательных элементов между максимальным и минимальным:", result)
