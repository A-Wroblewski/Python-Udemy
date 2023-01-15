def printao():
    print('a')
    print('a')
    print('a')

printao()
print()

def soma(x, y, z):
    print(x + y + z)

soma(9, 5, 6)
soma(y = 7, z = 3, x = 5)
soma(10, z = 2, y = 18)
print()

def oi(nome = 'insira um nome'):
    print(f'Olá, {nome}!')

oi('banana')
oi(8745843658734)
oi()
print()

def multiplicar(x, y, z = None):
    if z is not None:
        print(f'{x=} {y=} {z=}')
        print(x * y * z)

    else:
        print(f'{x=} {y=} {z=}')
        print(x * y)

multiplicar(3, 5)
multiplicar(2, 10)
multiplicar(2, 3, 4)
print()

variavel = 1

def funcao():
    variavel = 2

    def outra_funcao():
        variavel = 3

        print(variavel)

    outra_funcao()
    print(variavel)

print(variavel)
funcao()
print(variavel)
print()

def retorno_multiplicacao(x, y):
    return x * y

print(retorno_multiplicacao(5, 8))
print()

def outra_soma(*args):
    soma = 0

    for numero in args:
        soma += numero

    return f'{soma=}'

print(outra_soma(1, 2, 3, 6, 10, 15))
sominha = outra_soma(1, 2, 3, 6, 10)
print(sominha)
print(sum((1, 2, 3, 4, 5, 6, 7, 8)))

print()

numeros = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
pacotinho = outra_soma(*numeros)
print(pacotinho)
print(sum(numeros))
