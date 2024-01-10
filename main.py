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
        for i in n:
            if i % 2 == 0:
                res.append(i)
    elif b == 'odd':
        for i in n:
            if i % 2 != 0:
                res.append(i)
    else:
        if b == 'prime':
            for i in n:
                if is_prime(i) == True:
                    res.append(i)
    return res

a = range(1, 200)

print(filter_numbers(a, PRIME))
