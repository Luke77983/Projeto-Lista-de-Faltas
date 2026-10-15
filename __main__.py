from backend import Produto_repositorio
def main():
   repo = Produto_repositorio()

   print(repo.buscar("alicate"))

   


if __name__ == "__main__":
    main()
    
    
    
    