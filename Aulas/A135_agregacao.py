class CarrinhoDeCompras:
    def __init__(self):
        self._produtos = []

    def preco_total(self):
        return 'Total ->', sum([produto.preco for produto in self._produtos])

    def listar_produtos(self):
        for produto in self._produtos:
            print(produto.nome, produto.preco)

    def inserir_produtos(self, *produtos):
        for produto in produtos:
            self._produtos.append(produto)

class Produtos:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

carrinho_de_compras = CarrinhoDeCompras()

produto_1 = Produtos('Xícara', 4.99)
produto_2 = Produtos('Coquinha gelada', 2.99)
produto_3 = Produtos('Milka', 12.99)

carrinho_de_compras.inserir_produtos(produto_1, produto_2, produto_3)

carrinho_de_compras.listar_produtos()

print(*carrinho_de_compras.preco_total())
