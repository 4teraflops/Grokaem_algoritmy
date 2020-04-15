

def find_smallest(arr):  # поиск наименьшего элемента массива
    smallest = arr[0]  # Для хранения наименьшего значения
    smallest_index = 0  # Для хранения индекса наименьшего значения
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):  # сотрировка массива
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)  # Находит наименьший элемент в массиве и добавляет его в новый массив
        new_arr.append(arr.pop(smallest))
    return new_arr

arr = [5, 9, 45, 98, 4, 87, 65, 78, 7, 91]
print(selection_sort(arr))
