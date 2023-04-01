def executa_funcao(funcao, *args):
    return funcao(*args)

def soma(x, y):
    return x + y

# função soma em lambda
print(executa_funcao(lambda x, y: x + y, 4, 6))

print(executa_funcao(lambda *args: sum(args), 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
