import json
from A127_1_salvar_dados_da_classe import PATH, Person

with open(PATH, 'r', encoding='utf-8') as file:
    people = json.load(file)

print(*people, sep='\n')
print()

person_1 = Person(**people[0])
person_2 = people[1]

print(person_1.name)
print(person_1.age)
print(person_1.weight)
print(person_1.height, '\n')

print(person_2)
