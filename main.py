ODD = 'odd'
EVEN = 'even'
PRIME = 'prime'

def is_prime(a):
    if a % 2 == 0:
        return a == 2
    d = 3
    while d * d <= a and a % d != 0:
        d += 2
    return d * d > a
def filter_numbers(n, b):
    res = []
    if b == 'even':
        res = list(filter(lambda x: x % 2 == 0, n))
    elif b == 'odd':
        res = list(filter(lambda x: x % 2 != 0, n))
    else:
        if b == 'prime':
            res = list(filter(lambda x: x > 1 and x % 2 and x % 3 != 0, n))
    return res

a = range(1, 200)

print(filter_numbers(a, PRIME))
