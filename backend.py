import sqlite3
from pprint import pprint


class Produto:
    def __init__(self, id, codigo, produto, valor):
        self.id = id
        self.codigo = codigo
        self.nome = produto
        self.valor = valor


class Produto_repositorio:
    def __init__(self):
        conexao = sqlite3.connect("Lista_de_Faltas.db")
        self.conec = conexao
        cursor = self.conec.cursor()
        cursor.execute('''
        create table if not exists produtos(
                    id integer not null primary key autoincrement,
                    codigo int null,
                    produto varchar(30) not null ,
                    valor real not null
        )
''')

    def cadastrar(self, produto: str, valor: float):
        cursor = self.conec.cursor()

        cursor.execute('''
        insert into produtos (produto, valor) values(?,?)''',
        (produto, valor)
)
        self.conec.commit()

    def editar(self):
        cursor = self.conec.cursor()

        pprint(self.buscar())

        pesquisa = str(input("Digite um produto válido e confirme o id: "))

        print(self.buscar(pesquisa))

        while True:
            print('''
            Escolha uma opção para alterar:
            1 - Código do produto
            2 - Nome do produto
            3 - Valor do produto
            4 - Pesquisar novo produto
            5 - Deletar produto
            6 - Sair
    ''')

            opcao = int(input("Digite a opção: "))

            match opcao:

                case 1:
                    onde = "codigo"
                    id = int(input("Digite o id do produto: "))
                    nova_atualizacao = int(input("Digite novo código: "))
                case 2:
                    onde = "produto"
                    id = int(input("Digite o id do produto: "))
                    nova_atualizacao = str(input("Digite o novo nome do produto: "))
                case 3:
                    onde = "valor"
                    id = int(input("Digite o id do produto: "))
                    nova_atualizacao = float(input("Digite um novo valor: "))

                case 4:
                    pprint(self.buscar())
                    pesquisa = str(input("Digite um novo produto e confirme o id: "))
                    pprint(self.buscar(pesquisa))
                    continue
                case 5:
                    id = int(input("Digite a id do produto: "))
                    
                    resp = str(input("Tem certeza que deseja deletar esse produto? [S/N] ")).strip()
                    
                    if len(resp) == 0:
                        print("\033[31mOpção inválida\033[m")
                    
                        
                        
                    if resp == "S":
                        self.deletar(id)
                        continue
                    elif resp == "N":
                        continue
                    else:
                        print("\033[31mDigite uma opção valida\033[m]")
                        continue
                    
                    
                    
                case 6:
                    break
                case _:
                    print("\033[31mOpção invalida\033[m")
                    continue

            cursor.execute(f'''
            update produtos
            set  {onde} = ?
            where id = ?''', (nova_atualizacao, id,))

            if cursor.rowcount == 0:
                print("\033[31mid não encontrado\033[m")

            self.conec.commit()

    def buscar(self, produto=""):
        cursor = self.conec.cursor()
        cursor.execute('''
        select * from produtos
        where produto like ?''', (f"%{produto}%",))

        return cursor.fetchall()

    def deletar(self, idproduto):
        cursor = self.conec.cursor()
            
    

        cursor.execute('''
        delete  from produtos
        where id = ?''',
        (idproduto,))

        self.conec.commit()