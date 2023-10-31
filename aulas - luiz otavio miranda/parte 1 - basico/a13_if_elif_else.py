num_1 = 1
num_2 = 2

if num_1 > num_2 and num_1 < num_2:
    print('Verdadeiro1.')
elif num_1 < num_2 and num_1 != num_2:
    print('Verdadeiro2.')

if num_1 > num_2 or num_1 < num_2:
    print('Verdadeiro1.')
elif num_1 < num_2 or num_1 != num_2:
    print('Verdadeiro2.')

if not num_1 > num_2 and not num_1 < num_2:
    print('Verdadeiro1.')
elif not num_1 < num_2 and not num_1 != num_2:
    print('Verdadeiro2.')

if not num_1 > num_2 or not num_1 < num_2:
    print('Verdadeiro1.')
elif not num_1 < num_2 or not num_1 != num_2:
    print('Verdadeiro2.')

nome = 'Álvaro'

if 'var' in nome:
    print('Existe.')
else:
    print('Não existe.')

if 'banana' in nome:
    print('Existe.')
else:
    print('Não existe.')

if 'var' not in nome:
    print('Executado.')
else:
    print('Existe.')

if 'banana' not in nome:
    print('Executado.')
else:
    print('Existe.')

a = 'texto'
b = ''

if a:
    print('Variável preenchida!')
else:
    print('Variável vazia.')

if b:
    print('Variável preenchida!')
else:
    print('Variável vazia.')
