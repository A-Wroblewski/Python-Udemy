x = int(input('Type a number: '))
x = bin(x)

sum = 0

for number in x:
    if number == '1':
        sum += 1

print(sum)
