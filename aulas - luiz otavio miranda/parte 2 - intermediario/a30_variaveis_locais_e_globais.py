g = globals()
l = locals()

def concatenar(string_inicial):
    valor_final = string_inicial

    print(*l, sep='\n')

    def interna(string_para_concatenar):
        nonlocal valor_final
        
        valor_final += string_para_concatenar

        return valor_final
    
    return interna

string = concatenar('1')

print()
print(string('2'))
print(string('3'))
print(string('4'), '\n')

print(*g, sep='\n')
