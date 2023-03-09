def display_layout():
    row_letter = 0

    for row in seats:
        print(chr(row_letter + 97).upper(), row)

        row_letter += 1

    print(end='   ')

    columns_quantity = 10

    for column_number in range(columns_quantity):
        print(column_number + 1, end='  ')


# COMEÇO -> monta o layout todo zerado

seats = []

rows_quantity = 10

for empty_seat_state, row_letter in enumerate(range(rows_quantity)):
    empty_seat_state = 0

    seats.append([empty_seat_state] * rows_quantity)

# FIM -> monta o layout todo zerado

print()

while True:
    display_layout()

    row_input = input('\n\nChoose the row (A-J): ')
    column_input = int(input('Choose the column (1-10): '))

    aux_row_input = row_input.upper()  # salva a letra da fileira selecionada para mostra-lá no ticket
    fixed_column_input = column_input - 1  # diminui em 1 o valor da coluna para corresponder ao indíce

    row_input = row_input.lower()
    row_input = int(ord(row_input)) - 97

    if seats[row_input][fixed_column_input] == 0:
        print('\nIf you do not want to buy a ticket anymore, leave your name as empty.')
        name = input('Please enter your name (it will be displayed in your ticket): ')

        if not name:
            break

        seats[row_input][fixed_column_input] = 1

        print('\nThis seat is now yours!\n')

        print('-' * 20)
        print(f'Name: {name}')
        print('Movie: banana')
        print('Time: 14:30')
        print(f'Seat: {aux_row_input}{column_input}')
        print('-' * 20, '\n')

        buy_another = input('Do you want to buy another ticket? (type "N" to cancel) \n')

        if buy_another.upper() == 'N':
            break

    else:
        print('\nSeat occupied, please choose another one.\n')

print()
display_layout()
