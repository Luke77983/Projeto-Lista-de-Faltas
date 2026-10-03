import sqlite3

class Produto:
    def __init__(self,id,codigo ,  produto, valor):
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
        
       
    def cadastrar(self,produto:str, valor:float):
        cursor = self.conec.cursor()
         
        if self.buscar(produto) == []:
            cursor.execute('''
            insert into produtos (produto, valor) values(?,?)''',
            (produto, valor)
    )
            self.conec.commit()

    def editar(self):
        cursor = self.conec.cursor()
        pesquisa = str(input("Digite um produto válido e confirme o id: "))
        self.buscar(pesquisa)
        print('''
        Escolha uma opção para alterar:
        1 - Código do produto
        2 - Nome do produto
        3 - valor do produto
''')

        opcao = int(input("Digite a opção: "))
        match opcao:

            case 1:
                onde = "codigo"
                nova_atualizacao = int(input("Digite novo código: "))
            case 2: 
                onde = "produto"
                nova_atualizacao = str(input("Digite o novo nome do produto: "))
            case 3: 
                onde = "valor"
                nova_atualizacao = float(input("Digite um novo valor: "))

        
        
        

        id = int(input("Digite o id do produto: "))
        cursor.execute(f''' 
        update produtos
        set  {onde} = ?
        where id = {id}''', (nova_atualizacao,))

        self.conec.commit()

    def buscar(self,produto = ""):
        cursor = self.conec.cursor()
        cursor.execute('''
        select * from produtos
        where produto like ?''', (f"%{produto}%",))   
        
        print(cursor.fetchall())

    
    def deletar(self):
        pass
