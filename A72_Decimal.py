from decimal import Decimal

n1 = 0.3
n2 = 0.6
n3 = n1 + n2

print(n3)

print(f'{n3:.15f}')
print(f'{n3:.16f}')

print(round(n3, 15))

n4 = Decimal('0.3')
n5 = Decimal('0.6')
n6 = n4 + n5

print(n6)
