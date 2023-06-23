import timeit

def sum1(n):
    sum = 0

    for i in range(1, n + 1):
        sum += i

    return sum

print(timeit.timeit(stmt='sum1(100)', setup='from __main__ import sum1'))

def sum2(n):
    return (n * (n + 1)) / 2

print(timeit.timeit(stmt='sum2(100)', setup='from __main__ import sum2'))
