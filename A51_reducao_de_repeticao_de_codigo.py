velocidade_carro = 60
quilometro_carro = 99  # Exemplo: quilômetro 90 norte

LIMITE_RADAR_1 = 60
QUILOMETRO_RADAR_1 = 100
ALCANCE_RADAR_1 = 1

carro_passou_velocidade = velocidade_carro > LIMITE_RADAR_1
alcance_inicial_radar_1 = QUILOMETRO_RADAR_1 - ALCANCE_RADAR_1
alcance_final_radar_1 = QUILOMETRO_RADAR_1 + ALCANCE_RADAR_1
carro_no_alcance = quilometro_carro >= alcance_inicial_radar_1 and quilometro_carro <= alcance_final_radar_1

if carro_passou_velocidade:
    print('Seu carro está acima da velocidade permitida.')
else:
    print('Seu carro está dentro da velocidade permitida.')

if carro_no_alcance:
    print('Carro no alcance do radar 1.')
else:
    print('Carro fora do alcance do radar 1.')

if carro_no_alcance and carro_passou_velocidade:
    print('Carro multado no radar 1.')
else:
    print('Carro não multado no radar 1.')
