def quicksort(arr):  # Быстрая сортировка массива
    if len(arr) < 2:  # Базовый случай. Массивы с 0 и с 1 элементом уже "отсоритрованы"
        return arr
    else: # рекурсивный случай
        pivot = arr[0]  # Опорный элемент
        less = [i for i in arr[1:] if i <= pivot]  # Подмассив всех элементов, меньших опорного
        greater = [i for i in arr[1:] if i > pivot]  # подмассив всех элементов, больших опорного
        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([19, 56, 78, 11, 1, 98, 656, 4, 4, 8, 56, 45]))