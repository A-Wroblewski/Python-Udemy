def celsius_para_fahrenheit(celsius):
    fahrenheit = celsius * (9 / 5) + 32
    fahrenheit = round(fahrenheit, 2)

    return fahrenheit

def fahrenheit_para_celsius(fahrenheit):
    celsius = ((fahrenheit - 32) * 5) / 9
    celsius = round(celsius, 2)

    return celsius

escolha = int(input('Para converter celsius para fahrenheit, digite 1\n'
                    'Para converter fahrenheit para celsius, digite 2: '))

if escolha == 1:
    celsius = float(input('Digite a temperatura em celsius: '))

    print(celsius_para_fahrenheit(celsius), '°F')

elif escolha == 2:
    fahrenheit = float(input('Digite a temperatura em fahrenheit: '))

    print(fahrenheit_para_celsius(fahrenheit), '°C')

else:
    print('Digite 1 ou 2.')
