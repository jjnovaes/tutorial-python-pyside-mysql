# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TelaFuncionariouzDKJz.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_TelaFuncionario(object):
    def setupUi(self, TelaFuncionario):
        if not TelaFuncionario.objectName():
            TelaFuncionario.setObjectName(u"TelaFuncionario")
        TelaFuncionario.resize(509, 431)
        self.frame = QFrame(TelaFuncionario)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(11, 10, 491, 201))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.labelNome = QLabel(self.frame)
        self.labelNome.setObjectName(u"labelNome")
        self.labelNome.setGeometry(QRect(20, 46, 49, 16))
        self.lineEditNome = QLineEdit(self.frame)
        self.lineEditNome.setObjectName(u"lineEditNome")
        self.lineEditNome.setGeometry(QRect(80, 43, 111, 21))
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 83, 49, 16))
        self.comboBoxCargo = QComboBox(self.frame)
        self.comboBoxCargo.setObjectName(u"comboBoxCargo")
        self.comboBoxCargo.setGeometry(QRect(310, 78, 151, 24))
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(261, 81, 49, 16))
        self.lineEditCpf = QLineEdit(self.frame)
        self.lineEditCpf.setObjectName(u"lineEditCpf")
        self.lineEditCpf.setGeometry(QRect(50, 80, 111, 21))
        self.labelNome_2 = QLabel(self.frame)
        self.labelNome_2.setObjectName(u"labelNome_2")
        self.labelNome_2.setGeometry(QRect(30, 13, 49, 16))
        self.lineEditId = QLineEdit(self.frame)
        self.lineEditId.setObjectName(u"lineEditId")
        self.lineEditId.setGeometry(QRect(90, 10, 111, 21))
        self.frame_2 = QFrame(TelaFuncionario)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 216, 491, 44))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButtonExcluir = QPushButton(self.frame_2)
        self.pushButtonExcluir.setObjectName(u"pushButtonExcluir")

        self.horizontalLayout.addWidget(self.pushButtonExcluir)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButtonAlterar = QPushButton(self.frame_2)
        self.pushButtonAlterar.setObjectName(u"pushButtonAlterar")

        self.horizontalLayout.addWidget(self.pushButtonAlterar)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.pushButtonSalvar = QPushButton(self.frame_2)
        self.pushButtonSalvar.setObjectName(u"pushButtonSalvar")

        self.horizontalLayout.addWidget(self.pushButtonSalvar)

        self.tableWidgetFuncionarios = QTableWidget(TelaFuncionario)
        self.tableWidgetFuncionarios.setObjectName(u"tableWidgetFuncionarios")
        self.tableWidgetFuncionarios.setGeometry(QRect(10, 266, 491, 161))
        self.tableWidgetFuncionarios.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidgetFuncionarios.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidgetFuncionarios.horizontalHeader().setDefaultSectionSize(80)

        self.retranslateUi(TelaFuncionario)

        QMetaObject.connectSlotsByName(TelaFuncionario)
    # setupUi

    def retranslateUi(self, TelaFuncionario):
        TelaFuncionario.setWindowTitle(QCoreApplication.translate("TelaFuncionario", u"Chamado", None))
        self.labelNome.setText(QCoreApplication.translate("TelaFuncionario", u"Nome", None))
        self.label_3.setText(QCoreApplication.translate("TelaFuncionario", u"CPF", None))
        self.label_6.setText(QCoreApplication.translate("TelaFuncionario", u"Cargo", None))
        self.labelNome_2.setText(QCoreApplication.translate("TelaFuncionario", u"ID", None))
        self.pushButtonExcluir.setText(QCoreApplication.translate("TelaFuncionario", u"Excluir", None))
        self.pushButtonAlterar.setText(QCoreApplication.translate("TelaFuncionario", u"Alterar", None))
        self.pushButtonSalvar.setText(QCoreApplication.translate("TelaFuncionario", u"Salvar", None))
    # retranslateUi

