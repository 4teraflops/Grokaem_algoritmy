def binary_search(lst, itm):
    low = 0
    high = len(lst) - 1  # В переменных low и high хранятся границы той части списка, в которой выполняется поиск
    while low <= high:  # Пока эта часть не сократится  до одного элемента, проверяем средний элемент
        mid = (low + high) // 2  # делим целочисленным делением, чтоб не было ошибок типов данных
        guess = lst[mid]
        if guess == itm:  # если значение найдено
            return mid
        if guess > itm:  # много
            high = mid - 1
        else:  # мало
            low = mid + 1
    return None  # значения не существует


my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

print(binary_search(my_list, 105))