def countdowun(i):
    print(i)
    if i <= 0:  # Базовый случай
        return
    else:
        countdowun(i-1)  # Рекурсивный случай

countdowun(5)


def fact(x):  # Вычисление факториала (5! - факториал 5! = 5*4*3*2*1)
    if x == 1:
        return 1  # Базовый случай
    else:
        return x * fact(x-1)  # Рекурсивный случай


print(fact(3))