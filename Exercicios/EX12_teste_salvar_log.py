import json

def save():
    with open('EX12_teste_salvar_log.json', 'w', encoding='utf-8') as file:
        json.dump(stuff, file, ensure_ascii=False, indent=2)

stuff = []

while True:
    x = input('q = break / enter input: ')

    if x == 'q':
        break

    stuff.insert(0, x)
    save()

    if len(stuff) >= 10:
        stuff.pop()
