# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TelaLoginUAjPWK.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_TelaLogin(object):
    def setupUi(self, TelaLogin):
        if not TelaLogin.objectName():
            TelaLogin.setObjectName(u"TelaLogin")
        TelaLogin.resize(228, 153)
        self.labelUsuario = QLabel(TelaLogin)
        self.labelUsuario.setObjectName(u"labelUsuario")
        self.labelUsuario.setGeometry(QRect(97, 15, 41, 16))
        self.lineEditUsuario = QLineEdit(TelaLogin)
        self.lineEditUsuario.setObjectName(u"lineEditUsuario")
        self.lineEditUsuario.setGeometry(QRect(60, 30, 113, 21))
        self.lineEditSenha = QLineEdit(TelaLogin)
        self.lineEditSenha.setObjectName(u"lineEditSenha")
        self.lineEditSenha.setGeometry(QRect(60, 80, 113, 21))
        self.lineEditSenha.setEchoMode(QLineEdit.EchoMode.Password)
        self.pushButtonEntrar = QPushButton(TelaLogin)
        self.pushButtonEntrar.setObjectName(u"pushButtonEntrar")
        self.pushButtonEntrar.setGeometry(QRect(78, 116, 75, 24))
        self.labelSenha = QLabel(TelaLogin)
        self.labelSenha.setObjectName(u"labelSenha")
        self.labelSenha.setGeometry(QRect(100, 66, 31, 16))

        self.retranslateUi(TelaLogin)

        QMetaObject.connectSlotsByName(TelaLogin)
    # setupUi

    def retranslateUi(self, TelaLogin):
        TelaLogin.setWindowTitle(QCoreApplication.translate("TelaLogin", u"Login", None))
        self.labelUsuario.setText(QCoreApplication.translate("TelaLogin", u"Usu\u00e1rio", None))
        self.pushButtonEntrar.setText(QCoreApplication.translate("TelaLogin", u"Entrar", None))
        self.labelSenha.setText(QCoreApplication.translate("TelaLogin", u"Senha", None))
    # retranslateUi

