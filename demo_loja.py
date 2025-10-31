
from tabulate import tabulate
from loja_iniciante.modelos import Produto
from loja_iniciante.carrinho import Carrinho
def main():
# Produtos
    caderno = Produto("Caderno 10 matérias", 12.50)
    lapis = Produto("Lápis", 2.00)
    borracha = Produto("Borracha", 1.50)
    
    promo_caderno = caderno.desconto(20) # novo produto com 20% de desconto
    # Carrinho base
    carrinho = Carrinho()
    carrinho.adicionar(caderno, 1)
    carrinho.adicionar(lapis, 3)
    carrinho.adicionar(borracha, 1)
    # Teste dos operadores
    carrinho2 = carrinho + promo_caderno # novo carrinho com caderno em promoção
    carrinho3 = carrinho2 - lapis # novo carrinho removendo a primeira ocorrência de lápis
    carrinho += lapis # altera o próprio carrinho, adicionando um lápis
    carrinho -= borracha # altera o próprio carrinho, removendo a primeira ocorrência de borracha
    # Mostrar um carrinho final
    cabecalho = ["Produto", "Preço", "Qtd", "Subtotal"]
    print(tabulate(carrinho3.linhas_tabela(), headers=cabecalho, tablefmt="grid"))
    print("\nTotal carrinho 3: R$ {:.2f}".format(carrinho3.total()))
    print("Itens únicos carrinho 3:", carrinho3.itens_unicos())
if __name__ == "__main__":
    main()