import sqlite3
from pprint import pprint


class Produto:
    def __init__(self, id_produto= None, codigo = None, nome_produto = "", valor_produto = 0):
        self.id_produto = id_produto
        self.codigo = codigo
        self.nome_produto = nome_produto
        self.valor_produto = valor_produto




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

    def cadastrar(self, produto):
        cursor = self.conec.cursor()
        if self.buscar(produto) == []: 
            cursor.execute('''
            insert into produtos (produto, valor, codigo) values(?,?,?)''',
            (produto.nome_produto, produto.valor_produto, produto.codigo)
    )       
            novo_id = cursor.lastrowid
            
            self.conec.commit()
            
            return novo_id
        else:
            print("Erro esse produto já está cadastrado!")

    def editar(self,onde, nova_atualizacao, idproduto:int):
        cursor = self.conec.cursor()

                   
        cursor.execute(f'''
        update produtos
        set  {onde} = ?
        where id = ?''', (nova_atualizacao, idproduto))



        if cursor.rowcount == 0:
            return False
        else:
            self.conec.commit()
            return True

        

    def buscar(self, produto=""):
        cursor = self.conec.cursor()
        cursor.execute('''
        select * from produtos
        where produto like ?''', (f"%{produto}%",))

        lista = cursor.fetchall()
        lista_produtos = []
        for i in range(len(lista)):
            objeto_produto = Produto(lista[i][0], lista[i][1], lista[i][2], lista[i][3])
            lista_produtos.append(objeto_produto)
        return lista_produtos
            

    def deletar(self, idproduto):
        cursor = self.conec.cursor()
            
    

        cursor.execute('''
        delete  from produtos
        where id = ?''',
        (idproduto,))
        
        if cursor.rowcount == 0:
            return False
        else:
            self.conec.commit()
            return True