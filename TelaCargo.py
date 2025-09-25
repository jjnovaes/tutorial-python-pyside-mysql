# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TelaCargousRyxC.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_TelaCargo(object):
    def setupUi(self, TelaCargo):
        if not TelaCargo.objectName():
            TelaCargo.setObjectName(u"TelaCargo")
        TelaCargo.resize(506, 401)
        self.frame = QFrame(TelaCargo)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(11, 10, 491, 51))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 13, 49, 16))
        self.lineEditNome = QLineEdit(self.frame)
        self.lineEditNome.setObjectName(u"lineEditNome")
        self.lineEditNome.setGeometry(QRect(50, 10, 411, 21))
        self.frame_2 = QFrame(TelaCargo)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 176, 491, 44))
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

        self.tableWidgetCargos = QTableWidget(TelaCargo)
        self.tableWidgetCargos.setObjectName(u"tableWidgetCargos")
        self.tableWidgetCargos.setGeometry(QRect(10, 225, 491, 171))
        self.tableWidgetCargos.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tableWidgetCargos.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tableWidgetCargos.horizontalHeader().setDefaultSectionSize(99)

        self.retranslateUi(TelaCargo)

        QMetaObject.connectSlotsByName(TelaCargo)
    # setupUi

    def retranslateUi(self, TelaCargo):
        TelaCargo.setWindowTitle(QCoreApplication.translate("TelaCargo", u"Gerencia de Cargos", None))
        self.label_2.setText(QCoreApplication.translate("TelaCargo", u"Nome", None))
        self.pushButtonExcluir.setText(QCoreApplication.translate("TelaCargo", u"Excluir", None))
        self.pushButtonAlterar.setText(QCoreApplication.translate("TelaCargo", u"Alterar", None))
        self.pushButtonSalvar.setText(QCoreApplication.translate("TelaCargo", u"Salvar", None))
    # retranslateUi

