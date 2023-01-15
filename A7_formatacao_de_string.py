nome = 'Álvaro'
idade = 21
altura = 1.75
peso = 67
maior_de_idade = idade >= 18
imc = peso / altura ** 2

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('Peso:', str(peso) + ' kg')
print('É maior de idade:', maior_de_idade)

print()  # Exercício: print(nome idade imc)

print(nome, 'tem', idade, 'anos de idade e seu imc é de', str(imc) + '.')
print(f'{nome} tem {idade} anos de idade e seu imc é de {imc:.2f}.')
print('{} tem {} anos de idade e seu imc é de {:.2f}.'.format(nome, idade, imc))
print('{2} {0} tem {1} anos de idade {1} e seu imc é de {2:.2f}. {0}'.format(nome, idade, imc))
print('{n} tem {i} anos {n} de idade e seu {n} imc é de {im:.2f}.'.format(n = nome, i = idade, im = imc))
