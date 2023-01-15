espessura = int(input())
operacoes = int(input())
folhas = 1

for i in range(operacoes):
    folhas *= 2

pilha = folhas * espessura
print(pilha)
