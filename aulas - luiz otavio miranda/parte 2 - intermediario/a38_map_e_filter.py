def multiply_by_five(num):
    return num * 5

def is_even(num):
    return num % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

x = list(map(multiply_by_five, numbers))

print(x)

y = list(filter(is_even, numbers))

print(y, '\n')

# ambos passam uma função em todos os elementos de um iterável
# devem ser convertidos para usar o resultado obtido
# e para que iterador não esgote

# também funcionam com funções lambda

multiply_by_hundred = list(map(lambda num: num * 100, numbers))

print(multiply_by_hundred)

is_odd = list(filter(lambda num: num % 2 !=0, numbers))

print(is_odd)
