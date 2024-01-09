def numbers(n):
    res = []
    for i in n:
        i = i * i
        res.append(i)
    return res

a = (1, 4, 7, 12)

print(numbers(a))