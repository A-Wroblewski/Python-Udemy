num_1 = 7
num_2 = 6
divisao = num_1 / num_2

print(f'{divisao:.4f}')
print('{:.5f}'.format(divisao))

print()

numero = 15

print(f'{numero:0>5}')
print(f'{numero:a<5}')
print(f'{numero:X^5}')

print(f'{numero:k>10.3f}')
print(f'{numero:k<10.3f}')
print(f'{numero:k^10.3f}')

print()

nome = 'Álvaro Wroblewski rOChA'

print(f'{nome:M>30}')
print(f'{nome:M<30}')
print(f'{nome:M^30}')

print(nome.lower())
print(nome.upper())
print(nome.title())
print(nome.swapcase())
