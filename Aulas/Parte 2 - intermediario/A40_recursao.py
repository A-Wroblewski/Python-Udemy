def factorial(number):
    if number <= 1:  # caso base, previne loop infinito
        return number

    return number * factorial(number - 1)

result_factorial = factorial(6)

print(result_factorial, '\n')

def fibonacci(number):
    if number <= 1:
        return number
    
    return fibonacci(number - 1) + fibonacci(number - 2)

result_fibonacci = fibonacci(9)

print(result_fibonacci, '\n')

def sum_of_list_elements(list_value):
    if len(list_value) <= 0:
        return 0
    
    return list_value[0] + sum_of_list_elements(list_value[1:])

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(sum_of_list_elements(my_list))
