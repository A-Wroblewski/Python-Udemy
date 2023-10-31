try:
    a = 1
    b = 0

    print(a / b)

except ZeroDivisionError as erro:
    print(erro)

print()

try:
    print(c)

except NameError:
    print('Variável não definida.')

print()

# finally será executado sempre, independente de erros
#
# try:
#     print(10 / 0)
#
# finally:
#     print('Finally executado.')

try:
    print(10 / 0)

except:
    print('Erro.')

finally:
    print('Finally executado.')

print()

try:
    print(1)

except:
    print(2)

else:  # else executa somente se não houverem erros
    print(3)

finally:
    print(4)

print()

try:
    print(1)
    print(1 / 0)

except:
    print(2)

else:  # como ocorreu um erro, o else não será executado
    print(3)

finally:
    print(4)
