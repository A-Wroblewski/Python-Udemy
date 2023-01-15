class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta

class FerramentaDoEscritor:
    def __init__(self, ferramenta):
        self.ferramenta = ferramenta

    def escrever(self):
        return f'{self.ferramenta} está escrevendo...'

escritor = Escritor('Álvaro')
lapis = FerramentaDoEscritor('Lápis')
caneta = FerramentaDoEscritor('Caneta')

escritor.ferramenta = lapis

print(lapis.escrever())
print(caneta.escrever())
print(escritor.ferramenta.escrever())
