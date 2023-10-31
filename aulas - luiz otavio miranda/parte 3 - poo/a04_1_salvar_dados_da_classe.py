import json
from pathlib import Path

PATH = Path(__file__).parent / 'a04_3_dados_da_classe.json'

class Person:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

person_1 = Person('Álvaro', 21, 70, 1.75)
person_2 = Person('Nicolas', 20, 74, 1.77)

person_1_data = person_1.__dict__
person_2_data = person_2.__dict__

person_class_all_data = person_1_data, person_2_data

def do_dump():
    with open(PATH, 'w', encoding='utf-8') as file:
        json.dump(person_class_all_data, file, ensure_ascii=False, indent=2)

if __name__ == '__main__':  # executa as ações do bloco somente se este módulo for o primeiro a ser executado
    print(f'Name -> {person_1.name}')
    print(f'Age -> {person_1.age} years old')
    print(f'Weight -> {person_1.weight} kilos')
    print(f'Height -> {person_1.height} meters\n')

    print(f'Name -> {person_2.name}')
    print(f'Age -> {person_2.age} years old')
    print(f'Weight -> {person_2.weight} kilos')
    print(f'Height -> {person_2.height} meters')

    do_dump()
