def check_repeated_letters(word):
    stored_letters = set()

    for letter in word:
        if letter not in stored_letters:
            stored_letters.add(letter)
        
        else:
            return 'This word has repeated letters.'
    
    return 'This word has no repeated letters.'

word = input('Type your word: ').split()
word = ''.join(word)

print(check_repeated_letters(word))
