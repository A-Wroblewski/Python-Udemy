text = input()

print()

dictionary = {}

for letter in text:
    dictionary.update({letter: text.count(letter)})

for keys, values in dictionary.items():
    print(f'Letter = {keys} | Occurrences = {values}')
