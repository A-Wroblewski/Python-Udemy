# lembrar que as funções "inner" não retornam pois 
# elas e as decoradas printam o parâmetro direto

def decorator(func):
    def inner():
        print('------')
        func()
        print('------')

    return inner

@decorator  # aplica o decorador à função logo abaixo
def decorated_text():
    print('banana')

decorated_text()

print()

# Funcionamento do código abaixo:
#
# input "text" pedido
# função "display_text" recebe o input
# como há o decorador aplicado, o texto ainda não é printado
# decorador "uppercase_decorator" recebe a função "display_text"
# função "inner" pega o parâmetro anterior que vem junto com "text"
# "text" é transformado em uppercase
# texto decorado é printado pela função "display_text" ao ser chamada

def uppercase_decorator(func):
    def inner():
        func(text.upper())

    return inner

@uppercase_decorator
def display_text(text):
    print(text)

text = input('Type something: ')

display_text()
