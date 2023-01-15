def gerador():
    yield 1  # Pausa a execução da função no momento em que retorna o yield

    print('Continuando')

    yield 2

    print('De novo')

    yield 3

    print('Acabou!')

g = gerador()

print(g, '\n')

print(next(g))

print('banana')

print(next(g))
print(next(g))

print(1433472364725, '\n')

# print(next(g))  # StopIteration

def outro_gerador(n=1, maximo=10):
    while True:
        yield n
        n += 1

        if n > maximo:
            return

og = outro_gerador()

for n in og:
    print(n)

print()

def gen1():
    yield 1
    yield 2
    yield 3

def gen2():
    yield from gen1()

    yield 4
    yield 5
    yield 6

g1 = gen1()
g2 = gen2()

for n in g1:
    print(n)

print()

for n in g2:
    print(n)
