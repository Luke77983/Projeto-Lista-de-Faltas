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

    def editar(self,onde, nova_atualizacao, idproduto):
        cursor = self.conec.cursor()

                   
        cursor.execute(f'''
        update produtos
        set  {onde} = ?
        where id = ?''', (nova_atualizacao, idproduto,))



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

        return cursor.fetchall()

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