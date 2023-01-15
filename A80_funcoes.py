def multiplica(*args):
    total = 1

    for numero in args:
        total *= numero
    
    return f'Total = {total}'

print(multiplica(1, 2, 3, 4, 5, 6))

print()

def par_ou_impar(numero):
    par = numero % 2 == 0

    if par:
        return f'{numero} é par.'

    return f'{numero} é ímpar.'

print(par_ou_impar(1))
print(par_ou_impar(2))
print(par_ou_impar(3))
print(par_ou_impar(4))

print()

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    
    return saudar

dar_bom_dia = criar_saudacao('Bom dia')
dar_boa_noite = criar_saudacao('Boa noite')

print(dar_bom_dia('Júlia'))
print(dar_boa_noite('Ronaldo'))

for i in ['J', 'ú', 'l', 'i', 'a']:
    print(dar_boa_noite(i))
