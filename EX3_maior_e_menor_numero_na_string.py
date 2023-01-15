numbers = '8 3 -5 42 -1 0 0 -9 4 7 4 -4'

numbers = numbers.split(' ')

numbers = [int(num) for num in numbers]

print(max(numbers), min(numbers))
