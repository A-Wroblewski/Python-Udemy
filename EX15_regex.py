# https://www.rexegg.com/

import re

frase = 'Olá, meu número de telefone é (11)1234-5678'

r = re.search('\(\d{2}\)\d{4,5}-\d{4}', frase)

print(r, '\n')

###########################################################

frase = 'A placa de carro que eu anotei durante o acidente foi FRT-1998'

r = re.search('[A-Z]{3}-\d{4}', frase)

print(r, '\n')

###########################################################

frase = 'Entre em contato, meu email é teste@teste.com'

r = re.search('\w+@\w+\.\w+', frase)

print(r, '\n')

###########################################################

frase = 'Meu número de telefone atual é (11)1234-5678. O número (56)1111-1111 é o antigo'

r = re.findall('\(\d{2}\)\d{4,5}-\d{4}', frase)

print(r)
