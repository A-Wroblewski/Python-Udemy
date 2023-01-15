from math import sqrt

def bhaskara(a, b, c):
    delta = (b * b) - (4 * a * c)

    print(f'\nDelta = {delta}\n')

    if delta < 0:
        return 'Delta menor que 0, não há raízes reais.'

    x1 = (-b + sqrt(delta)) / (2 * a)
    x2 = (-b - sqrt(delta)) / (2 * a)

    return f'x1 = {x1:.2f}\nx2 = {x2:.2f}'

a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))

print(bhaskara(a, b, c))
