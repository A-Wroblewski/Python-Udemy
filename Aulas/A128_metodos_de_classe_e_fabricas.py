class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod  # não possuem self, referem-se à própria classe
    def metodo_da_classe(cls):
        print('oi')

    @classmethod
    def pessoa_com_50_anos(cls, nome):
        return cls(nome, 50)

    @classmethod
    def pessoa_anonima(cls, idade):
        return cls('Anônimo', idade)

p1 = Pessoa('nome', 100)
p2 = Pessoa.pessoa_com_50_anos('outro nome')
p3 = Pessoa.pessoa_anonima(20)

print(p1.nome, p1.idade)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)

Pessoa.metodo_da_classe()
