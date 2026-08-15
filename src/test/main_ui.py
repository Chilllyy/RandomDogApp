# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 841)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.buttonColorButton = QPushButton(self.centralwidget)
        self.buttonColorButton.setObjectName(u"buttonColorButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonColorButton.sizePolicy().hasHeightForWidth())
        self.buttonColorButton.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.buttonColorButton)

        self.guiColorButton = QPushButton(self.centralwidget)
        self.guiColorButton.setObjectName(u"guiColorButton")
        sizePolicy.setHeightForWidth(self.guiColorButton.sizePolicy().hasHeightForWidth())
        self.guiColorButton.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.guiColorButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.dogBreedList = QComboBox(self.centralwidget)
        self.dogBreedList.addItem("")
        self.dogBreedList.setObjectName(u"dogBreedList")
        self.dogBreedList.setStyleSheet(u"combobox-popup: 0;")
        self.dogBreedList.setMaxVisibleItems(10)

        self.horizontalLayout_4.addWidget(self.dogBreedList)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.dogSubBreedList = QComboBox(self.centralwidget)
        self.dogSubBreedList.addItem("")
        self.dogSubBreedList.setObjectName(u"dogSubBreedList")
        self.dogSubBreedList.setStyleSheet(u"combobox-popup: 0;")

        self.horizontalLayout_5.addWidget(self.dogSubBreedList)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.randomBreedButton = QPushButton(self.centralwidget)
        self.randomBreedButton.setObjectName(u"randomBreedButton")
        sizePolicy.setHeightForWidth(self.randomBreedButton.sizePolicy().hasHeightForWidth())
        self.randomBreedButton.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.randomBreedButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.dogImage = QLabel(self.centralwidget)
        self.dogImage.setObjectName(u"dogImage")
        sizePolicy.setHeightForWidth(self.dogImage.sizePolicy().hasHeightForWidth())
        self.dogImage.setSizePolicy(sizePolicy)
        self.dogImage.setMinimumSize(QSize(600, 600))
        self.dogImage.setMaximumSize(QSize(1280, 1280))
        self.dogImage.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.dogImage)

        self.nextButton = QPushButton(self.centralwidget)
        self.nextButton.setObjectName(u"nextButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.nextButton.sizePolicy().hasHeightForWidth())
        self.nextButton.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(42)
        font.setBold(True)
        self.nextButton.setFont(font)
        self.nextButton.setStyleSheet(u"background-color: green;")

        self.verticalLayout_3.addWidget(self.nextButton)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.buttonColorButton.setText(QCoreApplication.translate("MainWindow", u"Select Button Color", None))
        self.guiColorButton.setText(QCoreApplication.translate("MainWindow", u"Select GUI Color", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Dog Breed", None))
        self.dogBreedList.setItemText(0, QCoreApplication.translate("MainWindow", u"All", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Dog Sub Breed", None))
        self.dogSubBreedList.setItemText(0, QCoreApplication.translate("MainWindow", u"All", None))

        self.randomBreedButton.setText(QCoreApplication.translate("MainWindow", u"Random", None))
        self.dogImage.setText(QCoreApplication.translate("MainWindow", u"Dog Image", None))
        self.nextButton.setText(QCoreApplication.translate("MainWindow", u"Next Dog", None))
    # retranslateUi

