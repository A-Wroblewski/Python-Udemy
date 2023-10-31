string = 'pirarucu'

if hasattr(string, 'upper'):
    print(getattr(string, 'upper')())
    print(string)

print()

outra_string = 'peixe-boi'
metodo = 'title'

if hasattr(outra_string, metodo):
    print(getattr(outra_string, metodo)())

else:
    print(f'"{outra_string}" não possui o método {metodo}')

print()

print(dir(string))  # retorna os métodos do objeto pedido
