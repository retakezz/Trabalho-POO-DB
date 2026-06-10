import mysql.connector
from magos import *
from cavaleiros import *

conexao = mysql.connector.connect(host='localhost',
                                  database='magiaeaço_db',
                                  user='root',
                                  password='root')

if conexao.is_connected():
    print('Conexão bem-sucedida!')
    cursor = conexao.cursor()

Gandalf.salvar(cursor, conexao)
Douxie.salvar(cursor, conexao)
Dumbeldore.salvar(cursor, conexao)

Arthur.salvar(cursor, conexao)
Talion.salvar(cursor, conexao)
Steve.salvar(cursor, conexao)


print('Personagem salvo no banco de dados com sucesso!')

cursor.close()
conexao.close()