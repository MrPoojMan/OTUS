ODD = 'odd'
EVEN = 'even'
PRIME = 'prime'


def filter_numbers(n, a):
    res = []
    if a == 'even':
        for i in n:
            if i % 2 == 0:
                res.append(i)
    elif a == 'odd':
        for i in n:
            if i % 2 != 0:
                res.append(i)
    return res

a = [1, 2, 3, 4, 5, 6]

print(filter_numbers(a, ODD))
