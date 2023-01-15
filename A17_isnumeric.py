num_1 = input('Digite um número: ')
num_2 = input('Digite outro número: ')

if num_1.isnumeric() and num_2.isnumeric():
    num_1 = float(num_1)
    num_2 = float(num_2)

    print(num_1 + num_2)
else:
    print('Erro.')

try:
    num_1 = float(num_1)
    num_2 = float(num_2)

    print(num_1 + num_2)
except:
    print('Erro.')
