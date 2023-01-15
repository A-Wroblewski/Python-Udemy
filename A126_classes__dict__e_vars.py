class AnoDeNascimento:
    ANO_ATUAL = 2023  # atributo da classe

    def __init__(self, idade, enfeite):
        self.idade = idade
        self.enfeite = enfeite
    
    def ano_de_nascimento(self):
        return AnoDeNascimento.ANO_ATUAL - self.idade

print(f'Ano atual -> {AnoDeNascimento.ANO_ATUAL}')

idade_1 = AnoDeNascimento(21, 'banana')
print(idade_1.ano_de_nascimento())

idade_2 = AnoDeNascimento(50, 'maçã')
print(idade_2.ano_de_nascimento(), '\n')

print(idade_1.__dict__)
print(idade_2.__dict__, '\n')

idade_1.__dict__['outra'] = 'coisa'

print(vars(idade_2))
print(vars(idade_1))

del idade_1.outra

print(vars(idade_1), '\n')

dados_idade_1 = {'idade': 21, 'enfeite': 'banana'}
idade_1 = AnoDeNascimento(**dados_idade_1)

print(idade_1.idade)
print(idade_1.enfeite)
