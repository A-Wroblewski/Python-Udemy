class String(str):
    def upper(self):
        print('UPPER 1')

        coisa = super().upper()  # retorna o método da classe super, mesmo alterando ele

        print('UPPER 2')

        return coisa

string = String('banana')

print(string.upper(), '\n')

class A():  # classe A que herda o "object" (padrão).
    atributo_a = 'atributo a'

    def metodo(self):
        print('método a')

class B(A):  # classe B que herda a classe A
    atributo_b = 'atributo b'

    def metodo(self):
        print('método b')

class C(B):  # classe C que herda a classe B, que herda a classe A, logo tem acesso aos valores da classe A
    atributo_c = 'atributo c'

    def metodo(self):
        print('método c')

print(C.atributo_a)
print(C.atributo_b)
print(C.atributo_c)
