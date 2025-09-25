import sys
from PySide6 import QtWidgets
from TelaLogin import Ui_TelaLogin
from PySide6.QtWidgets import QMessageBox
from Principal import Principal
import Database

class Login(QtWidgets.QMainWindow, Ui_TelaLogin):
    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)
        # conectar o botão entrar com a função entrar
        self.pushButtonEntrar.clicked.connect(self.entrar)
    
    # função para validar o login e senha
    def entrar(self):
        try:
            #pegar os dados da tela
            usuario = self.lineEditUsuario.text()
            senha = self.lineEditSenha.text()
            
            #validar se os campos estão preenchidos
            if not usuario or not senha:
                QMessageBox.warning(self,"Atenção", "Preencha todos os campos")
                return
            #estabelecer a conexão com o banco de dados
            conexao = Database.conectar()
            #verificar se a conexão foi estabelecida
            if not conexao:
                QMessageBox.critical(self,"Atenção", "Erro ao conectar com o banco de dados")
                return
            #consultar o banco de dados para verificar se o usuário e senha estão corretos
            query = f"select * from usuario where usuario = '{usuario}' and senha = '{senha}'"
            cursor = conexao.cursor()
            cursor.execute(query)
            resultado = cursor.fetchall()
            #fechar a conexão com o banco de dados
            cursor.close()
            conexao.close()
            #verificar se o resultado da consulta retornou algum registro
            if resultado:
                #abrir a tela principal
                self.principal = Principal()
                self.principal.show()
                self.close() #fecha a tela atual
            else:
                QtWidgets.QMessageBox.critical(self,"Atenção", "Login ou senha incorretos")
        except Exception as erro:
            QtWidgets.QMessageBox.critical(self,"Atenção", "Ocorreu um erro ao validar")
            print('Erro:', erro)

app = QtWidgets.QApplication(sys.argv)
window = Login()
window.show()
app.exec()