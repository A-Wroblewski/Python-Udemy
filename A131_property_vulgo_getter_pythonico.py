class Caneta:
    def __init__(self, cor):
        self.cor_da_tinta = cor

    # def get_cor(self):  # protege o self para reduzir a quantidade de lugares afetados caso o nome mude
    #     print('Getter chamado.')
    #     return self.cor

    @property  # @property é um método que se comporta como atributo. É basicamente um getter no modo pythônico
    def cor(self):
        print('Property usada.')
        return self.cor_da_tinta

caneta = Caneta('Azul')

# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())

print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
