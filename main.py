ODD = 'odd'
EVEN = 'even'
PRIME = 'prime'

def is_prime(a):
    d = a - 1
    if d < 0:
        return False
    while d > 1:
        if a % d == 0:
            return False
        d -= 1
    return True

def filter_numbers(n, b):
    res = []
    if b == 'even':
        res = list(filter(lambda x: x % 2 == 0, n))
    elif b == 'odd':
        res = list(filter(lambda x: x % 2 != 0, n))
    else:
        if b == 'prime':
            res = list(filter(is_prime, n))
    return res

a = range(1, 200)

print(filter_numbers(a, PRIME))
