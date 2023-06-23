import timeit

def list1():
    list = []

    for i in range(100):
        list.append(i)

    return list

print(timeit.timeit(stmt='list1()', setup='from __main__ import list1'))

def list2():
    return range(100)

print(timeit.timeit(stmt='list2()', setup='from __main__ import list2'))
