def reverse_user_input(func):
    def inner():
        return func(user_input[::-1])

    return inner

@reverse_user_input
def display_user_input(user_input):
    return user_input

user_input = input('Type something: ')

display = display_user_input()

print(display, '\n')

# Função abaixo:
#
# "decorators_factory" pega os parâmetros do decorador
# "functions_factory" pega a função a ser decorada
# "inner" é a função que será executada

def decorators_factory(a=None, b=None, c=None):
    def functions_factory(func):
        # as funções decoradoras são executadas imediatamente ao serem chamadas
        print('decorator')
        
        def inner(*args):
            # como a função decorada vira a função interna da decoradora,
            # ela só é executada ao ser chamada
            print('inner')
            print('Args =', a, b, c)

            return func(*args)

        return inner

    return functions_factory

@decorators_factory()
def sum(x, y):
    return x + y

multiply = decorators_factory(1, 2, 3)(lambda x, y: x * y)

ten_plus_ten = sum(10, 10)
ten_times_ten = multiply(10, 10)

print(ten_plus_ten)
print(ten_times_ten)
