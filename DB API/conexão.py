import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / 'banco_da_Dani.db')
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

def criar_tabela(cursor):
    cursor.execute('CREATE TABLE clientes(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(100))')

def adiciona_user(cursor, conexao):
    nome = input('\nDigite seu nome: ')
    email = input('\nDigite seu email: ')
    data = (nome, email)
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?);", data)
    conexao.commit()

def alterar_valor(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute('UPDATE  clientes SET nome=?, email=? WHERE id=?', data)
    conexao.commit()

def deletar_registro(conexao, cursor, id):
    data = (id,)
    cursor.execute('DELETE FROM clientes WHERE id=?', data)
    conexao.commit()

def inserir_muitos(conexao, cursor, dados):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?,?)", dados)
    conexao.commit()

def recuperar_registros(cursor):
    
    cursor.execute('SELECT * FROM clientes')
    resultados = cursor.fetchall()
    for cliente in resultados:
        print(dict(cliente))

def recuperar_cliente(cursor, id):
    cursor.execute('SELECT * FROM clientes WHERE id=?', (id,))
    resultado = cursor.fetchone()
    print(dict(resultado))

dados = [
    ('Blahaj', 'blabla@gmail.com'),
    ('Daisy', 'daisyboco@gmail.com'),
    ('Romeo', 'remeobanana@gmail.com'),
    ('Dino', 'dinodini@gmail.com')
]


# inserir_muitos(conexao, cursor, dados)
# alterar_valor(conexao, cursor, 'Dani Melão', 'sapaiada@gmail.com', 1)
# deletar_registro(conexao, cursor, 1)
recuperar_registros(cursor)
recuperar_cliente(cursor, 2)