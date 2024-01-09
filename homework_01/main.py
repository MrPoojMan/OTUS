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


def filter_numbers(n):
    for i in n:
        if i % 2 == 0:
            return f"{n}{EVEN}"
        elif i % 2 != 0:
            return f"{n}{ODD}"
        else:
            return f"{n}{PRIME}"








    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """