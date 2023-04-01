print('Texto', type('Texto'))  # mostra o tipo de tal objeto
print(1, type(1))
print(1.0, type(1.0))
print(10 == 10, type(10 == 10))
print(10 == 11)

print('Texto', type('Texto'), bool('Texto'))
print('1', type('1'), type(int('1')))
print('1', type('1'), bool(type(int('1'))))

# todos os elementos abaixo são Falsy
print(bool())
print(bool(''))
print(bool(0))
print(bool(0.0))
print(bool([]))

print()  # Exercício:
# print('nome', type(''))
# print('idade', type(''))
# print('altura', type(''))
# print('maior de idade', type(''))

print('Álvaro', type('Álvaro'))
print(20, type(20))
print(1.75, type(1.75))
print(20 > 18, type(20 > 18))
