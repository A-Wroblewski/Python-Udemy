# Exercício usando o algoritmo de Luhn

import re

raw_credit_card_number = input('Enter the credit card numbers: ')
raw_credit_card_number = re.sub(r'[^0-9]', '', raw_credit_card_number)

if len(raw_credit_card_number) != 16:
    print('Your credit card number length must be of exactly 16 digits.')

else:
    raw_credit_card_number = raw_credit_card_number[::-1]
    credit_card_number = []

    for number in raw_credit_card_number:
        credit_card_number.append(int(number))

    credit_card_number[1::2] = [number * 2 for number in credit_card_number[1::2]]

    subtracted_credit_card_number = []

    for number in credit_card_number:
        if number > 9:
            number -= 9

        subtracted_credit_card_number.append(number)

    sum_of_credit_card_numbers = sum(subtracted_credit_card_number)

    if sum_of_credit_card_numbers % 10 == 0:
        print('This credit card number is valid.')

    else:
        print('This credit card number is not valid.')
