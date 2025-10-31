class Produto: 
    def __init__(self, nome, preco): 
        self.nome = nome
        self.preco = preco
    
    def desconto(self, percentual):
        novo_preco = self.preco * (1 - percentual/100)
        return Produto(self.nome, novo_preco)
    
    def __mul__(self, quantidade): 
        """ Subtotal deste produto para uma 'quantidade' inteira. """
        subtotal = self.preco * quantidade
        return subtotal
    
    def __repr__(self):
        """    Representação amigável: "Produto(nome='Caderno', preco=12.50)" """
        return f"Produto({self.nome} - {self.preco:.2f})"
