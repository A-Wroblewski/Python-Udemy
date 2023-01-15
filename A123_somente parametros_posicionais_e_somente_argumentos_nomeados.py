# todos os parâmetros antes da "/" devem ser argumentos posicionais
# todos os parâmetros depois do "*" devem ser argumentos nomeados

def soma(a, b, /, *, x, y):
    print(a + b + x + y)

soma(1, 2, y=3, x=4)
