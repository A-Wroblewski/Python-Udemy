text = input()
text = text.lower()

letters_with_more_than_one_occurrence = ''
my_set = set()

for letter in text:
    if letter not in my_set:
        my_set.add(letter)
    
    else:
        if letter in letters_with_more_than_one_occurrence:
            continue
        
        letters_with_more_than_one_occurrence += letter

quantity_of_letters_with_more_than_one_occurrence = 0

for _ in range(len(letters_with_more_than_one_occurrence)):
    quantity_of_letters_with_more_than_one_occurrence += 1

print(quantity_of_letters_with_more_than_one_occurrence)
