from pprint import pprint
from backend import *
def main():
   repo = Produto_repositorio()

   produto = Produto(None, None, "Martelo", 25)
   repo.cadastrar(produto)
   


if __name__ == "__main__":
    main()
    
    
    
    