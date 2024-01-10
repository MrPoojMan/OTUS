ODD = 'odd'
EVEN = 'even'
PRIME = 'prime'

def filter_numbers(n, a):
    res = []
    if a == 'even':
        for i in n:
            if i % 2 == 0:
                res.append(i)
    else:
        a == 'odd'
        for i in n:
            if i % 2 != 0:
                res.append(i)
    return res

