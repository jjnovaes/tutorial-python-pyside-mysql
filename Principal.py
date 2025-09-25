import sys
from PySide6 import QtWidgets
from TelaPrincipal import Ui_TelaPrincipal
from Cargo import Cargo

class Principal(QtWidgets.QMainWindow, Ui_TelaPrincipal):
    def __init__(self):
        super(Principal, self).__init__()
        self.setupUi(self)
        # conectar o menu cargo com a função abrirTelaCargo
        self.actionCargo.triggered.connect(self.abrirTelaCargo)
        # conectar o menu funcionário com a função abrirTelaFuncionario
        self.actionFuncionario.triggered.connect(self.abrirTelaFuncionario)
    
    # função para abrir a tela de cargo
    def abrirTelaCargo(self):
        self.cargo = Cargo()
        self.cargo.show()
    
    # função para abrir a tela de funcionário
    def abrirTelaFuncionario(self):
        pass

# app = QtWidgets.QApplication(sys.argv)
# window = Principal()
# window.show()
# app.exec()