frase = '     morangos     são vermelhos   '

print(frase.split())

print(''.join(frase))

print(frase.strip())

frase = frase.split()

print(''.join(frase))
print(' '.join(frase))
print('|'.join(frase))

frase2 = '     que dia mais, bonito  '

print(frase2.split(','))
print(frase2.split(', '))

print(frase2.lstrip())
print(frase2.rstrip())

print()

frase3 = '     banana com ,    mel  '
frase3_crua = frase3.split(',')

frase3_nova = []

for i, j in enumerate(frase3_crua):
    frase3_nova.append(frase3_crua[i].strip())

print(f'{frase3}|||{frase3_crua}|||{frase3_nova}')
