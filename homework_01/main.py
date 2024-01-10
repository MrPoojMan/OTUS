"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(n):
    res = []
    for i in n:
        i = i * i
        res.append(i)
    return res
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def filter_numbers(*n, b):
    res = []
    if b == 'even':
        res = list(filter(lambda x: x % 2 == 0, n))
    elif b == 'odd':
        res = list(filter(lambda x: x % 2 != 0, n))
    else:
        if b == 'prime':
            res = list(filter(lambda x: x > 1 and x % 2 and x % 3 != 0, n))
    return res


    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
