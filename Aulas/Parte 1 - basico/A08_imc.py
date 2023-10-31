from datetime import date

nome = 'Álvaro'
idade = 21
altura = 1.75
peso = 67
imc = peso / altura ** 2
ano_atual = date.today()

print(f'{nome} tem {idade} anos de idade, {altura} de altura e pesa {peso} kg.')
print(f'Ele tem um imc de {imc:.2f} e nasceu em {(ano_atual.year - idade) - 1}.')
