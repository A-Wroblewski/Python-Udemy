# esses modificadores de acesso são apenas convenção, já que não existem no Python.

class Class:
    def __init__(self):
        self.publico = 'Público.'  # pode ser usado em qualquer lugar
        self._protegido = 'Protegido.'  # só deve ser usado naquela classe ou nas subclasses
        self.__privado = 'Privado.'  # só deve ser usado na classe em que foi declarado

    def metodo_publico(self):
        return 'Método público.'

    def _metodo_protegido(self):
        return 'Método protegido.'

    def __metodo_privado(self):
        return 'Método privado.'

x = Class()

print(x.publico)
print(x.metodo_publico(), '\n')

print(x._protegido)  # não usar fora da classe ou subclasses
print(x._metodo_protegido(), '\n')  # não usar fora da classe ou subclasses

# por se tratar de um atributo privado, a própria linguagem muda o nome dela
# para evitar usos fora da classe, porém ainda pode ser acessada.
#
# print(x.__privado)
# print(x.__metodo_privado)
print(x._Class__metodo_privado())  # name mangling (desfiguração de nomes)
