var1 = 'banana'
var2 = 'banana'
var3 = 'maçã'

print(id(var1))
print(id(var2))
print(id(var3))

print()

condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True

print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)

if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')
