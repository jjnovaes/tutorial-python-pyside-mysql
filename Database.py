import mysql.connector as mysql

def conectar():
    conexao = mysql.connect(
        host='localhost',
        port='3306',
        user='root',
        password='',
        database='rh_db'
    )
    return conexao
