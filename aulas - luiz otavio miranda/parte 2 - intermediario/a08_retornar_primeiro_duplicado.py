lista_com_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],  # -1
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],  # indice 3
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],  # indice 3
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],  # indice 7
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],  # indice 2
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],  # indice 5
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],  # indice 6
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],  # indice 2
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],  # indice 3
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],  # indice 6
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],  # indice 4
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],  # -1
]

def encontrar_primeiro_duplicado():
    numeros_checados = set()
    numero_duplicado = -1

    for numero in lista:
        if numero in numeros_checados:
            numero_duplicado = numero
            break

        numeros_checados.add(numero)
    
    return numero_duplicado

for lista in lista_com_listas_de_inteiros:
    print(lista, encontrar_primeiro_duplicado())
