class Pessoa:
    def __init__(self, nome, sobrenome):  # sempre reservar o primeiro parâmetro para o "self"
        self.nome = nome  # self seria o mesmo que a variável
        self.sobrenome = sobrenome

pessoa_1 = Pessoa('Álvaro', 'Wroblewski')  # ao chamar a classe, uma nova instância é criada
# pessoa_1.nome = 'Álvaro'
# pessoa_1.sobrenome = 'Wroblewski'

print(pessoa_1)
print(pessoa_1.nome)
print(pessoa_1.sobrenome, '\n')

pessoa_2 = Pessoa('Ante', 'deguemon')
# pessoa_2.nome = 'Ante'
# pessoa_2.sobrenome = 'deguemon'

print(pessoa_2)
print(pessoa_2.nome)
print(pessoa_2.sobrenome, '\n')

class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} começou a acelerar...')

ferrari = Carro('Ferrari')
print(f'Carro -> {ferrari.nome}')

ferrari.acelerar()

print()

porsche = Carro('Porsche')
print(f'Carro -> {porsche.nome}')

porsche.acelerar()
