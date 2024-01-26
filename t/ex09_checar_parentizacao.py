def check_parenthesis(phrase):
    open_parenthesis = 0
    closed_parenthesis = 0
    last_parenthesis = ''

    for letter in phrase:
        if letter == '(':
            open_parenthesis += 1
            last_parenthesis = letter
        
        if letter == ')':
            closed_parenthesis += 1
            last_parenthesis = letter
        
    if (open_parenthesis == closed_parenthesis and last_parenthesis == ')') or (open_parenthesis == 0 and closed_parenthesis == 0):
        return 'Correct parenting.'

    return 'Incorrect parenting.'

phrase = input('Type your phrase: ')

print(check_parenthesis(phrase))
