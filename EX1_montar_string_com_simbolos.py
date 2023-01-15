string = input()

first_digit = int(string[0])
second_digit = int(string[1])

new_string = ''

if first_digit == 0 and second_digit == 0:
    print('Empty.')

else:
    for number in range(first_digit):
        new_string += '#'

    for number in range(second_digit):
        new_string += '*'

    print(new_string)
