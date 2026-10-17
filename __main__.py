from pprint import pprint
from backend import *
def main():
   repo = Produto_repositorio()



   for c in repo.buscar():
       print(c.id_produto, c.nome_produto)
   
   repo.deletar(999)
   
  
if __name__ == "__main__":
    main()
    
    
    
    