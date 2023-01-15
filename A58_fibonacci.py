def fibonacci(_):
    number_1, number_2 = 0, 1
    counter = 0

    while counter < user_number:
        print(number_1)

        next_number = number_1 + number_2
        number_1 = number_2
        number_2 = next_number
        counter += 1

user_number = int(input('Choose a number: '))

fibonacci(user_number)
