import json
from pathlib import Path

pessoa = {
    'Nome': 'Álvaro',
    'Sobrenome': 'Wroblewski',
    'Idade': 21,
    'Altura': 1.75,
    'Endereços': [
        {
            'Lugar 1': 'eni ayuoki',
            'Número': 123,
        },
        {
            'Lugar 2': 'Rua dos Bobos',
            'Número': 0,
        },
    ],
    'Homem': True,
    'nada': None,
}

path = Path(__file__).parent / 'a42_json.json'

# encoding e ensure_ascii para mostrar texto corretamente
with open(path, 'w', encoding='utf-8') as file:
    json.dump(pessoa, file, ensure_ascii=False, indent=2)  # armazena objetos em um json

with open(path, 'r', encoding='utf-8') as file:
    dados = json.load(file)  # retorna um objeto do json
    
    for chave, valor in dados.items():
        print(f'{chave}: {valor}')
