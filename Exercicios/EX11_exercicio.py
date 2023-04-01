# REGRAS:
#
# se o número é par, então (número / 2)
# se o número é ímpar, então (3 * número + 1)

number = int(input('Choose your number: '))

while number != 1:
    if number % 2 == 0:
        number //= 2

        print(number, end=' ')

    else:
        number = 3 * number + 1
        
        print(number, end=' ')
