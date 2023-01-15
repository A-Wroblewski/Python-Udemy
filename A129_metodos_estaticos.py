class Classe:
    @staticmethod  # não possuem self nem cls
    def funcao_dentro_da_classe(*args, **kwargs):
        return 'Oi!', args, kwargs

x = Classe.funcao_dentro_da_classe(1, 2, 3, banana='banana')

print(x)
