class Caneta:
    def __init__(self, cor):
        self._cor = cor  # atributos que começam com underline são privados daquela classe e não devem ser usados fora dela

    @property
    def cor(self):
        print('Property usada.')
        return self._cor

    @cor.setter
    def cor(self, valor):
        self._cor = valor

caneta = Caneta('Azul')

print(caneta.cor)

caneta.cor = 'Rosa'

print(caneta.cor)
