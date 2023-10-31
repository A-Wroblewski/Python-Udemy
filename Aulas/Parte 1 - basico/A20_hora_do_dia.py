# Exercício: baseado no horário dado, cumprimentar de acordo

hora = input('Que horas são? ')

if hora.isdecimal():
    hora = int(hora)

    if hora >= 0 and hora <= 11:
        print('Bom dia!')
    elif hora > 11 and hora <= 17:
        print('Boa tarde!')
    elif hora > 17 and hora <= 23:
        print('Boa noite!')
    else:
        print('Essa hora não existe.')
else:
    print('Essa hora não existe.')
