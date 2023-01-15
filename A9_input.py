nome = input('Qual é o seu nome? ')
idade = input('Qual é a sua idade? ')
ano_nascimento = 2023 - int(idade)

print()

print(f'O nome do usuário é {nome}, ele tem {idade} anos de idade e nasceu em {ano_nascimento - 1}.\n'
      f'Os tipos das variáveis são {type(nome)}, {type(idade)} e {type(ano_nascimento)}.')
