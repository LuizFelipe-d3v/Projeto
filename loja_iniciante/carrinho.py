from tabulate import tabulate

class Carrinho:
    def __init__(self): 
        self.itens = []


    def adicionar(self, produto, quantidade = 1):
        self.itens.append((produto, quantidade))

    def remover(self, produto_retirar):
        for item in self.itens:
            if item == produto_retirar:
                self.itens.pop(item)
                break
    
    def itens_unicos(self):
        vistos = []
        for item in self.itens:
            if item not in vistos:
                vistos.append(item)
        return vistos

    def total(self):
        subtotal = 0
        total = 0
        for item, quantidade in self.itens:
            subtotal = item.preco * quantidade
            total += subtotal
        return total

    def linhas_tabela(self):
        linhas = []
        for item, quantidade in self.itens:
            subtotal = item.preco * quantidade
            linhas.append([item.nome, f"R$ {item.preco:.2f}", quantidade, f"R$ {subtotal:.2f}"])
        return linhas
    
    def __add__(self, produto_novo):
        novo_carrinho = Carrinho()
        produto_existe = False
        for produto, quantidade in self.itens:
            if produto == produto_novo:
                novo_carrinho.adicionar(produto, quantidade + 1)
            else:
                novo_carrinho.adicionar(produto, quantidade)
            if not produto_existe:
                novo_carrinho.adicionar(produto_novo)
        return novo_carrinho
        
        

    def __sub__(self, produto_novo):
        novo_carrinho = Carrinho()
        produto_removido = False
        for produto, quantidade in self.itens:
            if produto == produto_novo and not produto_removido:
                if quantidade > 1:
                    novo_carrinho.adicionar(produto, quantidade - 1)
                produto_removido = True
            else:
                novo_carrinho.adicionar(produto, quantidade)
        return novo_carrinho
     
    def __iadd__(self, produto_novo):
        self.adicionar(produto_novo, 1)
        return self

    def __isub__(self, produto):
        self.remover(produto)
        return self

    