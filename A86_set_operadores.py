s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}

print(s1 | s2)  # união dos sets

print(s1 & s2)  # intersecção dos sets

print(s1 - s2)  # diferença (itens somente no set da esquerda)
print(s2 - s1)

print(s1 ^ s2)  # diferença simétrica (itens que não estão em ambos os sets)
