# o python usa C3 superclass linearization para gerar a ordem MRO
# https://en.wikipedia.org/wiki/C3_linearization

class A:
    ...

    def classe(self):
        print('A')

class B(A):
    ...

    # def classe(self):
    #     print('B')

class C(A):
    ...

    def classe(self):
        print('C')

class D(B, C):  # a primeira classe passada na herança sempre vai ser a primeira checada
    ...

    # def classe(self):
    #     print('D')

d = D()

d.classe()

# mostram o MRO
print(D.__mro__, '\n')
print(D.mro())
