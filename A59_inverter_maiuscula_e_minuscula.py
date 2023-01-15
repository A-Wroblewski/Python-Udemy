def swap_case(string): 
    new_string = ''
    
    for i in string:
        if i.islower():
            new_string += i.upper()
        else:
            new_string += i.lower()
            
    return new_string

string = input()
result = swap_case(string)

print(result)
