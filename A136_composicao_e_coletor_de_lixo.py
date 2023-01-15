class Pessoa:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        # como os endereços foram criados dentro da classe Pessoa, quando a pessoa for deletado os endereços seram removidos juntamente com ela
        self.enderecos.append(Endereco(rua, numero))

class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print('Deletando', self.rua, self.numero)

pessoa = Pessoa('Antedeguemon')

pessoa.inserir_endereco('Avenida Brasil', 123)
pessoa.inserir_endereco('rua', 1)

print(pessoa.enderecos[0].rua, pessoa.enderecos[0].numero)
print(pessoa.enderecos[1].rua, pessoa.enderecos[1].numero)

# del pessoa

print('\nfim do código\n')
