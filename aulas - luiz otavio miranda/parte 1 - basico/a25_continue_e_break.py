x = 0

while x <= 10:
    print(x)
    x += 1

print('Acabou!¹')

print()

y = 0

while y <= 10:
    if y == 3 or y == 5 or y == 8:
        y += 1
        continue

    print(y)
    y += 1

print('Acabou!²')

print()

z = 0

while z <= 10:
    if z == 6:
        break

    print(z)
    z += 1

print('Acabou!³')
