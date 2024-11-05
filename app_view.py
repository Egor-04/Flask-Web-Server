# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QLabel

from flask_web_server import web_request


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1921, 1080)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.logoSpace = QtWidgets.QFrame(self.centralwidget)
        self.logoSpace.setGeometry(QtCore.QRect(0, 0, 1921, 91))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logoSpace.sizePolicy().hasHeightForWidth())
        self.logoSpace.setSizePolicy(sizePolicy)
        self.logoSpace.setStyleSheet("background-color: rgb(113, 153, 161);")
        self.logoSpace.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logoSpace.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logoSpace.setObjectName("logoSpace")
        self.label = QtWidgets.QLabel(self.logoSpace)
        self.label.setGeometry(QtCore.QRect(0, 10, 241, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setLineWidth(1)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.logoSpace)
        self.lineEdit.setGeometry(QtCore.QRect(230, 20, 1531, 51))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    background-color: white; /* Цвет фона кнопки */\n"
"    border: none; /* Убираем обводку */\n"
"    color: white; /* Цвет текста */\n"
"    border-radius: 12%; /* Установка радиуса обводки на 50% для округления кнопки */\n"
"    width: 100px; /* Ширина кнопки */\n"
"    height: 100px; /* Высота кнопки */\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.logoSpace)
        self.pushButton.setGeometry(QtCore.QRect(1770, 20, 51, 51))
        self.pushButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Online_Electronics_Store/Images/Search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(50, 50))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_Menu = QtWidgets.QPushButton(self.logoSpace)
        self.pushButton_Menu.setGeometry(QtCore.QRect(1840, 20, 61, 41))
        self.pushButton_Menu.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.pushButton_Menu.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Online_Electronics_Store/Images/Menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Menu.setIcon(icon1)
        self.pushButton_Menu.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_Menu.setObjectName("pushButton_Menu")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 160, 1371, 871))
        self.scrollArea.setAcceptDrops(False)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1352, 869))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 1331, 831))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_container = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_container.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_container.setObjectName("gridLayout_container")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.frame_Menu = QtWidgets.QFrame(self.centralwidget)
        self.frame_Menu.setGeometry(QtCore.QRect(1550, 90, 371, 951))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.frame_Menu.setFont(font)
        self.frame_Menu.setStyleSheet("")
        self.frame_Menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Menu.setObjectName("frame_Menu")
        self.label_Username = QtWidgets.QLabel(self.frame_Menu)
        self.label_Username.setGeometry(QtCore.QRect(110, 20, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_Username.setFont(font)
        self.label_Username.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_Username.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Username.setObjectName("label_Username")
        self.label_AvatarRect = QtWidgets.QLabel(self.frame_Menu)
        self.label_AvatarRect.setGeometry(QtCore.QRect(0, 0, 371, 91))
        self.label_AvatarRect.setStyleSheet("background-color: rgb(113, 153, 161);")
        self.label_AvatarRect.setText("")
        self.label_AvatarRect.setObjectName("label_AvatarRect")
        self.label_PhoneNumber = QtWidgets.QLabel(self.frame_Menu)
        self.label_PhoneNumber.setGeometry(QtCore.QRect(120, 50, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_PhoneNumber.setFont(font)
        self.label_PhoneNumber.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_PhoneNumber.setAlignment(QtCore.Qt.AlignCenter)
        self.label_PhoneNumber.setObjectName("label_PhoneNumber")
        self.label_Avatar = QtWidgets.QLabel(self.frame_Menu)
        self.label_Avatar.setGeometry(QtCore.QRect(20, 10, 61, 61))
        self.label_Avatar.setText("")
        self.label_Avatar.setPixmap(QtGui.QPixmap("C:/Users/Егор Михайловский/Downloads/Avatar.png"))
        self.label_Avatar.setScaledContents(True)
        self.label_Avatar.setObjectName("label_Avatar")
        self.label_background = QtWidgets.QLabel(self.frame_Menu)
        self.label_background.setGeometry(QtCore.QRect(0, 90, 371, 111))
        self.label_background.setStyleSheet("\n"
"background-color: rgba(162, 193, 200, 200);")
        self.label_background.setText("")
        self.label_background.setObjectName("label_background")
        self.pushButton_Cart = QtWidgets.QPushButton(self.frame_Menu)
        self.pushButton_Cart.setGeometry(QtCore.QRect(10, 120, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_Cart.setFont(font)
        self.pushButton_Cart.setStyleSheet("QPushButton {\n"
"    background-color: rgb(145, 181, 186);\n"
"    border: none; /* Убираем обводку */\n"
"    color: white; /* Цвет текста */\n"
"    border-radius: 12%; /* Установка радиуса обводки на 50% для округления кнопки */\n"
"    width: 100px; /* Ширина кнопки */\n"
"    height: 100px; /* Высота кнопки */\n"
"}")
        self.pushButton_Cart.setObjectName("pushButton_Cart")
        self.pushButton_Registration = QtWidgets.QPushButton(self.frame_Menu)
        self.pushButton_Registration.setGeometry(QtCore.QRect(10, 890, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_Registration.setFont(font)
        self.pushButton_Registration.setStyleSheet("QPushButton {\n"
"    background-color: rgb(145, 181, 186);\n"
"    border: none; /* Убираем обводку */\n"
"    color: white; /* Цвет текста */\n"
"    border-radius: 12%; /* Установка радиуса обводки на 50% для округления кнопки */\n"
"    width: 100px; /* Ширина кнопки */\n"
"    height: 100px; /* Высота кнопки */\n"
"}")
        self.pushButton_Registration.setObjectName("pushButton_Registration")
        self.pushButton_LogIn = QtWidgets.QPushButton(self.frame_Menu)
        self.pushButton_LogIn.setGeometry(QtCore.QRect(10, 830, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_LogIn.setFont(font)
        self.pushButton_LogIn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(145, 181, 186);\n"
"    border: none; /* Убираем обводку */\n"
"    color: white; /* Цвет текста */\n"
"    border-radius: 12%; /* Установка радиуса обводки на 50% для округления кнопки */\n"
"    width: 100px; /* Ширина кнопки */\n"
"    height: 100px; /* Высота кнопки */\n"
"}")
        self.pushButton_LogIn.setObjectName("pushButton_LogIn")
        self.frame_Cart = QtWidgets.QFrame(self.frame_Menu)
        self.frame_Cart.setEnabled(True)
        self.frame_Cart.setGeometry(QtCore.QRect(-1, 89, 371, 851))
        self.frame_Cart.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Cart.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Cart.setObjectName("frame_Cart")
        self.label_background_cart = QtWidgets.QLabel(self.frame_Cart)
        self.label_background_cart.setGeometry(QtCore.QRect(-4, 2, 381, 851))
        self.label_background_cart.setStyleSheet("background-color: rgb(179, 203, 209);")
        self.label_background_cart.setText("")
        self.label_background_cart.setObjectName("label_background_cart")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame_Cart)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 371, 851))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_Cart = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_Cart.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_Cart.setObjectName("verticalLayout_Cart")
        self.pushButton_Close_Cart = QtWidgets.QPushButton(self.frame_Cart)
        self.pushButton_Close_Cart.setGeometry(QtCore.QRect(130, 790, 81, 41))
        self.pushButton_Close_Cart.setStyleSheet("QPushButton {\n"
"    font: 16pt \"MS Shell Dlg 2\";\n"
"    \n"
"    background-color: rgb(185, 222, 231);\n"
"    border: none; /* Убираем обводку */\n"
"    color: black; /* Цвет текста */\n"
"    border-radius: 12%; /* Установка радиуса обводки на 50% для округления кнопки */\n"
"    width: 100px; /* Ширина кнопки */\n"
"    height: 100px; /* Высота кнопки */\n"
"}")
        self.pushButton_Close_Cart.setObjectName("pushButton_Close_Cart")
        self.label_AvatarRect.raise_()
        self.label_PhoneNumber.raise_()
        self.label_Username.raise_()
        self.label_Avatar.raise_()
        self.label_background.raise_()
        self.pushButton_Cart.raise_()
        self.pushButton_Registration.raise_()
        self.pushButton_LogIn.raise_()
        self.frame_Cart.raise_()
        self.product_item_1 = QtWidgets.QFrame(self.centralwidget)
        self.product_item_1.setGeometry(QtCore.QRect(1390, 320, 231, 221))
        self.product_item_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.product_item_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.product_item_1.setObjectName("product_item_1")
        self.label_background_1 = QtWidgets.QLabel(self.product_item_1)
        self.label_background_1.setGeometry(QtCore.QRect(6, 2, 221, 211))
        self.label_background_1.setStyleSheet("QFrame {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: none; /* Убираем обводку */\n"
"    color: white; /* Цвет текста */\n"
"    border-radius: 12%; /* Установка радиуса обводки на 50% для округления кнопки */\n"
"    width: 100px; /* Ширина кнопки */\n"
"    height: 100px; /* Высота кнопки */\n"
"}")
        self.label_background_1.setText("")
        self.label_background_1.setObjectName("label_background_1")
        self.Icon = QtWidgets.QLabel(self.product_item_1)
        self.Icon.setGeometry(QtCore.QRect(40, 10, 151, 121))
        self.Icon.setAutoFillBackground(False)
        self.Icon.setText("")
        self.Icon.setPixmap(QtGui.QPixmap("../Online_Electronics_Store/Images/Monitor.jpg"))
        self.Icon.setScaledContents(True)
        self.Icon.setWordWrap(False)
        self.Icon.setObjectName("Icon")
        self.pushButton_1_ = QtWidgets.QPushButton(self.product_item_1)
        self.pushButton_1_.setGeometry(QtCore.QRect(40, 160, 151, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_1_.setFont(font)
        self.pushButton_1_.setStyleSheet("QPushButton {\n"
"    \n"
"    background-color: rgb(185, 222, 231);\n"
"    border: none; /* Убираем обводку */\n"
"    color: black; /* Цвет текста */\n"
"    border-radius: 12%; /* Установка радиуса обводки на 50% для округления кнопки */\n"
"    width: 100px; /* Ширина кнопки */\n"
"    height: 100px; /* Высота кнопки */\n"
"}")
        self.pushButton_1_.setFlat(False)
        self.pushButton_1_.setObjectName("pushButton_1_")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1921, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Online Electronics Store"))
        self.label.setText(_translate("MainWindow", "Electro-NX"))
        self.label_Username.setText(_translate("MainWindow", "User - 12349042"))
        self.label_PhoneNumber.setText(_translate("MainWindow", "+79338839675"))
        self.pushButton_Cart.setText(_translate("MainWindow", "Cart"))
        self.pushButton_Registration.setText(_translate("MainWindow", "Registration"))
        self.pushButton_LogIn.setText(_translate("MainWindow", "Log In"))
        self.pushButton_Close_Cart.setText(_translate("MainWindow", "<--"))
        self.pushButton_1_.setText(_translate("MainWindow", "Add to Bascket"))



####################################################################################
        self.notification_count = 0
        self.frame_Menu.hide()
        self.frame_Cart.hide()

        # Web Server Responses
        self.load_products()

        #Products Items
        self.gridLayout_container.addWidget(self.product_item_1)

        #Buttons Actions
        self.pushButton_1_.clicked.connect(self.add_to_cart)

        self.pushButton_Menu.clicked.connect(self.open_menu)

        self.pushButton_Cart.clicked.connect(self.open_close_cart)
        self.pushButton_Close_Cart.clicked.connect(self.open_close_cart)

        # Effects
        effect1 = QGraphicsDropShadowEffect(
            offset=QPoint(0, 5), blurRadius=8, color=QColor("#a2a2a2")
        )
        self.product_item_1.setGraphicsEffect(effect1)

    def add_to_cart(self):
        self.notification_count += 1
        message = 'Товар успешно добавлен в корзину!'
        notification = Notification(message, self.notification_count, self)
        notification.show_notification()

    def decrement_counter(self):
        self.notification_count = 0


    def open_menu(self):
        if self.frame_Menu.isVisible():
            self.frame_Menu.hide()
        else:
            self.frame_Menu.show()

    def open_close_cart(self):
        if self.frame_Cart.isVisible():
            self.frame_Cart.hide()
        else:
            self.frame_Cart.show()

    def load_products(self):
        try:
            response = web_request()  # URL сервера Flask
            response.raise_for_status()
            products = response.json()
            print(products)

            # Очистка предыдущих виджетов перед добавлением новых
            for widget in self.gridLayout_container.children():
                widget.deleteLater()

            # Добавление новых продуктов в QGridLayout
            for idx, (product_id, product_name) in enumerate(products):
                self.gridLayout_container.addWidget(QLabel(f'Product ID: {product_id} | Name: {product_name}', self.gridLayoutWidget))

        except web_request().exceptions.RequestException as e:
            print(e)

# Доп. Классы
class Notification(QtWidgets.QDialog):

    def __init__(self, message, notification_count, notification_manager):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)

        # Установка размеров уведомления
        self.setGeometry(600, 500 + (notification_count * 70), 250, 60)

        # Установка QVBoxLayout
        layout = QtWidgets.QVBoxLayout(self)
        self.label = QtWidgets.QLabel(message)
        self.label.setStyleSheet(
            """
            background-color: white;     /* Белый фон */
            border: 2px solid #799fa5;  /* Зеленая рамка */
            border-radius: 10px;        /* Скругленные края */
            padding: 10px;              /* Отступы внутри лейбла */
            font-size: 14px;            /* Размер шрифта */
            """)
        self.label.setWordWrap(True)
        layout.addWidget(self.label)
        self.setLayout(layout)
        print(notification_count)

        # Установка начального положения уведомления (ниже экрана)
        screen_geometry = QtWidgets.QDesktopWidget().screenGeometry()
        self.setGeometry(screen_geometry.width() - 270, screen_geometry.height() - (notification_count * 70) - 70,
                         self.width(), self.height())

        # Анимация всплытия
        self.animation = QtCore.QPropertyAnimation(self, b"pos")
        self.animation.setDuration(500)
        self.animation.setStartValue(QPoint(screen_geometry.width() - self.width() - 20, screen_geometry.height()))
        self.animation.setEndValue(QPoint(screen_geometry.width() - self.width() - 20,
                                          screen_geometry.height() - (notification_count * 90) - 70))

        # Установка таймера для удаления уведомления через 4 секунды
        self.timer = QtCore.QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(lambda: self.remove_notification(notification_manager))
        self.timer.start(4000)


    def remove_notification(self, notification_manager):
        notification_manager.decrement_counter()
        self.deleteLater()


    def show_notification(self):
        self.show()
        self.animation.start()  # Запустить анимацию при показе уведомления



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
