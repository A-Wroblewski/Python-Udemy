inteiro = 0
flutuante = 0.0
string = ''
lista = []
tupla = ()
dicionario = {}
conjunto = set()
falso = False
nenhum = None
intervalo = range(0)

def falseta(item):
    return 'Falsy' if not item else 'Truthy'

print(f'{inteiro} = {falseta(inteiro)}')
print(f'{flutuante} = {falseta(flutuante)}')
print(f'{string} = {falseta(string)}')
print(f'{lista} = {falseta(lista)}')
print(f'{tupla} = {falseta(tupla)}')
print(f'{dicionario} = {falseta(dicionario)}')
print(f'{conjunto} = {falseta(conjunto)}')
print(f'{falso} = {falseta(falso)}')
print(f'{nenhum} = {falseta(nenhum)}')
print(f'{intervalo} = {falseta(intervalo)}')
