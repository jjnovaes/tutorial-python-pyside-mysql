# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TelaPrincipalAFCOLg.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_TelaPrincipal(object):
    def setupUi(self, TelaPrincipal):
        if not TelaPrincipal.objectName():
            TelaPrincipal.setObjectName(u"TelaPrincipal")
        TelaPrincipal.resize(800, 600)
        self.actionCargo = QAction(TelaPrincipal)
        self.actionCargo.setObjectName(u"actionCargo")
        self.actionSobre = QAction(TelaPrincipal)
        self.actionSobre.setObjectName(u"actionSobre")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DialogQuestion))
        self.actionSobre.setIcon(icon)
        self.actionFuncionario = QAction(TelaPrincipal)
        self.actionFuncionario.setObjectName(u"actionFuncionario")
        self.centralwidget = QWidget(TelaPrincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        TelaPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(TelaPrincipal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuArquivo = QMenu(self.menubar)
        self.menuArquivo.setObjectName(u"menuArquivo")
        self.menuAjuda = QMenu(self.menubar)
        self.menuAjuda.setObjectName(u"menuAjuda")
        TelaPrincipal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(TelaPrincipal)
        self.statusbar.setObjectName(u"statusbar")
        TelaPrincipal.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menubar.addAction(self.menuAjuda.menuAction())
        self.menuArquivo.addAction(self.actionCargo)
        self.menuArquivo.addAction(self.actionFuncionario)
        self.menuAjuda.addAction(self.actionSobre)

        self.retranslateUi(TelaPrincipal)

        QMetaObject.connectSlotsByName(TelaPrincipal)
    # setupUi

    def retranslateUi(self, TelaPrincipal):
        TelaPrincipal.setWindowTitle(QCoreApplication.translate("TelaPrincipal", u"Sistema gerenciador de chamados", None))
        self.actionCargo.setText(QCoreApplication.translate("TelaPrincipal", u"Cargo", None))
        self.actionSobre.setText(QCoreApplication.translate("TelaPrincipal", u"Sobre", None))
        self.actionFuncionario.setText(QCoreApplication.translate("TelaPrincipal", u"Funcion\u00e1rio", None))
        self.menuArquivo.setTitle(QCoreApplication.translate("TelaPrincipal", u"Arquivo", None))
        self.menuAjuda.setTitle(QCoreApplication.translate("TelaPrincipal", u"Ajuda", None))
    # retranslateUi

