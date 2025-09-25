import sys
from PySide6 import QtWidgets
from TelaCargo import Ui_TelaCargo
import Database

class Cargo(QtWidgets.QMainWindow, Ui_TelaCargo):
    def __init__(self):
        super(Cargo, self).__init__()
        self.setupUi(self)
        self.pushButtonSalvar.clicked.connect(self.salvar)
        self.resultado = []
        self.montarTabela()
        self.tableWidget.cellClicked.connect(self.selecionar)
        self.item_selecionado = "" #começa com valor vazio
        self.pushButtonExcluir.clicked.connect(self.excluir)
        self.pushButtonAlterar.clicked.connect(self.alterar)

    def salvar(self):
        try:
            nome = self.lineEditNome.text()
            email = self.lineEditEmail.text()
            login = self.lineEditLogin.text()
            senha = self.lineEditSenha.text()

            if not nome or not email or not login or not senha:
                QtWidgets.QMessageBox.warning(self,"Atenção", "Preencha todos os campos")
                return

            conexao = Database.conectar()
            cursor = conexao.cursor()
            query = f"insert into tecnico (nome, email, login, senha) values ('{nome}', '{email}', '{login}', '{senha}')"                
            cursor.execute(query)
            conexao.commit()
            conexao.close()
            self.montarTabela()
            QtWidgets.QMessageBox.warning(self,"Sucesso", "Inserido com sucesso")
            self.limpar()
        except Exception as erro:
            QtWidgets.QMessageBox.critical(self,"Atenção", "Erro ao inserir dados")
            print('Erro:', erro)
    
    def montarTabela(self):
        try:
            conexao = Database.conectar()
            query = "select * from tecnico"
            cursor = conexao.cursor()
            cursor.execute(query)
            self.resultado = cursor.fetchall()
            conexao.close()
            linha = 0
            self.tableWidget.setRowCount(len(self.resultado))
            # print(len(self.resultado))
            for item in self.resultado:
                self.tableWidget.setItem(linha, 0, QtWidgets.QTableWidgetItem(str(item[0]))) #id
                self.tableWidget.setItem(linha, 1, QtWidgets.QTableWidgetItem(item[1])) #nome
                self.tableWidget.setItem(linha, 2, QtWidgets.QTableWidgetItem(item[2])) #email
                self.tableWidget.setItem(linha, 3, QtWidgets.QTableWidgetItem(item[3])) #usuario
                self.tableWidget.setItem(linha, 4, QtWidgets.QTableWidgetItem(item[4])) #senha
                linha+=1
        except Exception as erro:
            QtWidgets.QMessageBox.critical(self,"Atenção", "Erro ao buscar dados")
            print('Erro:', erro)
    
    #identiciar a linha que o usuario clicou na tabela
    #para assim podermos excluir ou alterar
    def selecionar(self):
        #recuperando o id da linha selecionada
        id = self.tableWidget.currentRow()
        #print(id)
        self.item_selecionado = self.resultado[id]
        #print(self.item_selecionado)
        #print(self.item_selecionado[1])
        self.lineEditId.setText(str(self.item_selecionado[0]))
        self.lineEditNome.setText(self.item_selecionado[1])
        self.lineEditEmail.setText(self.item_selecionado[2])
        self.lineEditLogin.setText(self.item_selecionado[3])
        self.lineEditSenha.setText(self.item_selecionado[4])

    def excluir(self):
        try:
            resposta = QtWidgets.QMessageBox.question(self,"Atenção", "Deseja realmente excluir")
            if resposta == QtWidgets.QMessageBox.Yes:
                conexao = Database.conectar()
                cursor = conexao.cursor()                
                query = f"delete from tecnico where idtecnico = {self.item_selecionado[0]}"
                cursor.execute(query)
                conexao.commit()
                conexao.close()
                self.montarTabela()
                QtWidgets.QMessageBox.warning(self,"Sucesso", "Excluido com sucesso")
                self.limpar()
        except Exception as erro:
            QtWidgets.QMessageBox.critical(self,"Atenção", "Erro ao excluir dados")
            print('Erro:', erro)
    
    def alterar(self):
        try:
            id = int(self.lineEditId.text())
            nome = self.lineEditNome.text()
            email = self.lineEditEmail.text()
            login = self.lineEditLogin.text()
            senha = self.lineEditSenha.text()
            if not nome or not email or not login or not senha:
                QtWidgets.QMessageBox.warning(self,"Atenção", "Preencha todos os campos")
                return
            conexao = Database.conectar()
            cursor = conexao.cursor()
            query = f"""update tecnico set nome = '{nome}', email = '{email}',
            login = '{login}', senha = '{senha}' where idtecnico = {id}"""
            cursor.execute(query)
            conexao.commit()
            conexao.close()
            self.montarTabela()
            QtWidgets.QMessageBox.warning(self,"Sucesso", "Alterado com sucesso")
            self.limpar()
        except Exception as erro:
            QtWidgets.QMessageBox.critical(self,"Atenção", "Erro ao inserir dados")
            print('Erro:', erro)
    
    def limpar(self):
        self.lineEditId.clear()
        self.lineEditNome.clear()
        self.lineEditEmail.clear()
        self.lineEditLogin.clear()
        self.lineEditSenha.clear()

# app = QtWidgets.QApplication(sys.argv)
# window = Tecnico()
# window.show()
# app.exec()