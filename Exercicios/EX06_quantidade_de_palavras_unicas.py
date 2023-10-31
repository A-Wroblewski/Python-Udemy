def unique_word(phrase):
    stored_words = set()

    for word in phrase:
        if word not in stored_words:
            stored_words.add(word)

    return len(stored_words)

phrase = input('Type your phrase: ').split()

amount_of_unique_words = unique_word(phrase)

print(f'\nThe amount of unique words is: {amount_of_unique_words}')
