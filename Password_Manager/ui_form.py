# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QListView,
    QMainWindow, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(800, 600))
        MainWindow.setStyleSheet(u"#centralwidget{\n"
"	background-color: #ffffff;\n"
"	border-radius: 15px; \n"
"}\n"
"\n"
".QLabel{\n"
"		font-family: \"Roboto\";\n"
"}\n"
"\n"
".Line{\n"
"	background-color: rgba(128, 128, 128, 128); /* Gris suave con 50% de opacidad */\n"
"    border: 1px solid #B0B0B0; /* Borde gris claro */\n"
"    color: #000000; /* Color del texto negro */\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 30))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.AddButton = QPushButton(self.frame_3)
        self.AddButton.setObjectName(u"AddButton")
        self.AddButton.setGeometry(QRect(10, 0, 28, 28))
        self.AddButton.setStyleSheet(u"    background-color: #90D7FF; /* Fondo azul */\n"
"    color: #000000; /* Texto blanco */\n"
"    border-radius: 8px; /* Radio del borde para hacer el bot\u00f3n circular */\n"
"    border: 2px solid  #90D7FF; /* Borde del mismo color que el fondo */\n"
"    min-width: 24px; /* Ancho m\u00ednimo */\n"
"    min-height: 24px; /* Altura m\u00ednima */\n"
"    max-width: 24px; /* Ancho m\u00e1ximo */\n"
"    max-height: 24px; /* Altura m\u00e1xima */\n"
"")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.AddButton.setIcon(icon)
        self.menu = QPushButton(self.frame_3)
        self.menu.setObjectName(u"menu")
        self.menu.setGeometry(QRect(740, 0, 31, 31))
        self.menu.setStyleSheet(u"border: 2px;\n"
"border-radius: 10px;\n"
"    background-color: #ffffff; \n"
"")
        icon1 = QIcon()
        icon1.addFile(u"../../Desktop/2\u00baDAM/images/dots.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.menu.setIcon(icon1)
        self.menu.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.frame_3, 0, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.listView = QListView(self.frame_4)
        self.listView.setObjectName(u"listView")

        self.verticalLayout_4.addWidget(self.listView)


        self.horizontalLayout.addWidget(self.frame_4)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)

        self.line_2 = QFrame(self.frame_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_3.addWidget(self.line_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(9, 0, -1, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setSpacing(4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(3, 0, 3, 3)
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"#frame_7 {\n"
"  border: 2px solid #000;\n"
"  border-radius: 15px;\n"
"  background-color: rgba(200, 200, 200, 0.5); /* Gris claro y medio transparente */\n"
"}\n"
"")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_7)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(9, -1, -1, -1)
        self.frame_16 = QFrame(self.frame_7)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_11.setSpacing(3)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(3, 3, 3, 3)
        self.label_5 = QLabel(self.frame_16)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_11.addWidget(self.label_5)

        self.horizontalSpacer_4 = QSpacerItem(47, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_4)

        self.nombre = QLineEdit(self.frame_16)
        self.nombre.setObjectName(u"nombre")

        self.horizontalLayout_11.addWidget(self.nombre)


        self.verticalLayout_11.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_7)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_12.setSpacing(3)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(3, 3, 3, 3)
        self.label_6 = QLabel(self.frame_17)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_12.addWidget(self.label_6)

        self.horizontalSpacer_5 = QSpacerItem(70, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_5)

        self.url = QLineEdit(self.frame_17)
        self.url.setObjectName(u"url")

        self.horizontalLayout_12.addWidget(self.url)


        self.verticalLayout_11.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.frame_7)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_13.setSpacing(3)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(3, 3, 3, 3)
        self.label_8 = QLabel(self.frame_18)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_13.addWidget(self.label_8)

        self.horizontalSpacer_6 = QSpacerItem(60, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_6)

        self.notas = QLineEdit(self.frame_18)
        self.notas.setObjectName(u"notas")

        self.horizontalLayout_13.addWidget(self.notas)


        self.verticalLayout_11.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.frame_7)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_14.setSpacing(3)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(3, 3, 3, 3)
        self.label_7 = QLabel(self.frame_19)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_14.addWidget(self.label_7)

        self.horizontalSpacer_7 = QSpacerItem(30, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_7)

        self.password = QLineEdit(self.frame_19)
        self.password.setObjectName(u"password")

        self.horizontalLayout_14.addWidget(self.password)


        self.verticalLayout_11.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.frame_7)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_20)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.mostrar_contrasena = QCheckBox(self.frame_20)
        self.mostrar_contrasena.setObjectName(u"mostrar_contrasena")

        self.verticalLayout_10.addWidget(self.mostrar_contrasena)


        self.verticalLayout_11.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.frame_7)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.crear = QPushButton(self.frame_21)
        self.crear.setObjectName(u"crear")

        self.horizontalLayout_15.addWidget(self.crear)

        self.modificar = QPushButton(self.frame_21)
        self.modificar.setObjectName(u"modificar")

        self.horizontalLayout_15.addWidget(self.modificar)

        self.eliminar = QPushButton(self.frame_21)
        self.eliminar.setObjectName(u"eliminar")

        self.horizontalLayout_15.addWidget(self.eliminar)


        self.verticalLayout_11.addWidget(self.frame_21)


        self.verticalLayout_8.addWidget(self.frame_7)

        self.line_3 = QFrame(self.frame_6)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_8.addWidget(self.line_3)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"  #frame_9{\n"
"  border: 2px solid #000;\n"
"    border-radius: 15px;\n"
"    background-color: #a5d8ff;\n"
"\n"
"}\n"
"")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.contrasena = QLabel(self.frame_10)
        self.contrasena.setObjectName(u"contrasena")
        self.contrasena.setStyleSheet(u"    font-size: 10pt;\n"
"    font-weight: bold;\n"
"\n"
"")

        self.verticalLayout_7.addWidget(self.contrasena)

        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_2 = QLabel(self.frame_12)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_8.addWidget(self.label_2)

        self.letras_checkbox = QCheckBox(self.frame_12)
        self.letras_checkbox.setObjectName(u"letras_checkbox")
        self.letras_checkbox.setChecked(True)

        self.horizontalLayout_8.addWidget(self.letras_checkbox)

        self.horizontalSpacer = QSpacerItem(259, 19, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.copiar = QPushButton(self.frame_12)
        self.copiar.setObjectName(u"copiar")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditPaste))
        self.copiar.setIcon(icon2)

        self.horizontalLayout_8.addWidget(self.copiar)


        self.verticalLayout_7.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_10)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_3 = QLabel(self.frame_13)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_7.addWidget(self.label_3)

        self.numeros_checkbox = QCheckBox(self.frame_13)
        self.numeros_checkbox.setObjectName(u"numeros_checkbox")

        self.horizontalLayout_7.addWidget(self.numeros_checkbox)

        self.horizontalSpacer_2 = QSpacerItem(123, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

        self.frame_11 = QFrame(self.frame_13)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_11)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_15 = QFrame(self.frame_11)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_10.setSpacing(35)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_15)
        self.label.setObjectName(u"label")

        self.horizontalLayout_10.addWidget(self.label)

        self.sliderL = QLabel(self.frame_15)
        self.sliderL.setObjectName(u"sliderL")

        self.horizontalLayout_10.addWidget(self.sliderL)


        self.verticalLayout_9.addWidget(self.frame_15)

        self.slider = QSlider(self.frame_11)
        self.slider.setObjectName(u"slider")
        self.slider.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_9.addWidget(self.slider)


        self.horizontalLayout_7.addWidget(self.frame_11)


        self.verticalLayout_7.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_10)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_4 = QLabel(self.frame_14)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_9.addWidget(self.label_4)

        self.caracteres_checkbox = QCheckBox(self.frame_14)
        self.caracteres_checkbox.setObjectName(u"caracteres_checkbox")

        self.horizontalLayout_9.addWidget(self.caracteres_checkbox)

        self.horizontalSpacer_3 = QSpacerItem(121, 19, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_3)

        self.generarB = QPushButton(self.frame_14)
        self.generarB.setObjectName(u"generarB")

        self.horizontalLayout_9.addWidget(self.generarB)


        self.verticalLayout_7.addWidget(self.frame_14)


        self.horizontalLayout_6.addWidget(self.frame_10)

        self.horizontalLayout_6.setStretch(0, 1)

        self.horizontalLayout_4.addWidget(self.frame_9)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)


        self.verticalLayout_8.addWidget(self.frame_8)


        self.verticalLayout_5.addWidget(self.frame_6)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)


        self.horizontalLayout_2.addWidget(self.frame_5)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 3)

        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_2)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 14)

        self.verticalLayout.addWidget(self.frame)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.AddButton.setText("")
        self.menu.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"URL", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Notas", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.mostrar_contrasena.setText(QCoreApplication.translate("MainWindow", u"Mostrar contrase\u00f1a", None))
        self.crear.setText(QCoreApplication.translate("MainWindow", u"Crear", None))
        self.modificar.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
        self.eliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.contrasena.setText(QCoreApplication.translate("MainWindow", u"Generador de Contrase\u00f1as", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Letras (por ejemplo, Aa)", None))
        self.letras_checkbox.setText("")
        self.copiar.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"N\u00fameros (por ejemplo, 2, 3, 4)", None))
        self.numeros_checkbox.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Longitud ", None))
        self.sliderL.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Caracteres especiales (por ejemplo !@$)", None))
        self.caracteres_checkbox.setText("")
        self.generarB.setText(QCoreApplication.translate("MainWindow", u"Generar", None))
    # retranslateUi

