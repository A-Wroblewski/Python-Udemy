for x in range(11):
    print(x)

print('Acabou!¹')

print()

for y in range(11):
    if y == 3 or y == 5 or y == 8:
        continue

    print(y)

print('Acabou!²')

print()

for z in range(11):
    if z == 6:
        break

    print(z)

print('Acabou!³')
