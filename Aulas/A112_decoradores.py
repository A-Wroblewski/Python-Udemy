# ordem de aplicação dos decoradores -> de baixo para cima

def decorators_factory(name):
    def functions_factory(func):
        print('Decorator:', name)

        def inner(*args):
            x = func(*args)

            return f'{x} {name}'

        return inner

    return functions_factory

@decorators_factory('third decorator')
@decorators_factory('second decorator')
@decorators_factory('first decorator')
def hi(x):
    return 'hi ' + x

greetings = hi('banana')

print(greetings)
