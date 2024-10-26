from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsDropShadowEffect


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.logoSpace = QtWidgets.QFrame(self.centralwidget)
        self.logoSpace.setGeometry(QtCore.QRect(0, 0, 1921, 91))
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
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: white; /* Цвет фона кнопки */\n"
"    border: none; /* Убираем обводку */\n"
"    color: white; /* Цвет текста */\n"
"    border-radius: 12%; /* Установка радиуса обводки на 50% для округления кнопки */\n"
"    width: 100px; /* Ширина кнопки */\n"
"    height: 100px; /* Высота кнопки */\n"
"    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3), /* Тень снизу для выпуклости */\n"
"                0px 1px 1px rgba(255, 255, 255, 0.5); /* Светлая тень сверху */\n"
"    transition: all 0.3s; /* Плавный переход для изменяющихся эффектов */\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 110, 1371, 921))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1369, 919))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.product_1 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.product_1.setGeometry(QtCore.QRect(10, 10, 232, 215))
        self.product_1.setStyleSheet("QGroupBox {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: none; /* Убираем обводку */\n"
"    color: white; /* Цвет текста */\n"
"    border-radius: 12%; /* Установка радиуса обводки на 50% для округления кнопки */\n"
"    width: 100px; /* Ширина кнопки */\n"
"    height: 100px; /* Высота кнопки */\n"
"}")
        self.product_1.setTitle("")
        self.product_1.setObjectName("product_1")
        self.label_13 = QtWidgets.QLabel(self.product_1)
        self.label_13.setGeometry(QtCore.QRect(40, 10, 151, 121))
        self.label_13.setAutoFillBackground(False)
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("C:/Users/Егор Михайловский/Downloads/6308924095.jpg"))
        self.label_13.setScaledContents(True)
        self.label_13.setWordWrap(False)
        self.label_13.setObjectName("label_13")
        self.pushButton_1_ = QtWidgets.QPushButton(self.product_1)
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
        self.product_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.product_2.setGeometry(QtCore.QRect(270, 10, 232, 215))
        self.product_2.setStyleSheet("QGroupBox {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: none; /* Убираем обводку */\n"
"    color: white; /* Цвет текста */\n"
"    border-radius: 12%; /* Установка радиуса обводки на 50% для округления кнопки */\n"
"    width: 100px; /* Ширина кнопки */\n"
"    height: 100px; /* Высота кнопки */\n"
"}")
        self.product_2.setTitle("")
        self.product_2.setObjectName("product_2")
        self.label_14 = QtWidgets.QLabel(self.product_2)
        self.label_14.setGeometry(QtCore.QRect(40, 10, 151, 121))
        self.label_14.setAutoFillBackground(False)
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("C:/Users/Егор Михайловский/Downloads/6308924095.jpg"))
        self.label_14.setScaledContents(True)
        self.label_14.setWordWrap(False)
        self.label_14.setObjectName("label_14")
        self.pushButton_1_1 = QtWidgets.QPushButton(self.product_2)
        self.pushButton_1_1.setGeometry(QtCore.QRect(40, 160, 151, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_1_1.setFont(font)
        self.pushButton_1_1.setStyleSheet("QPushButton {\n"
"    \n"
"    background-color: rgb(185, 222, 231);\n"
"    border: none; /* Убираем обводку */\n"
"    color: black; /* Цвет текста */\n"
"    border-radius: 12%; /* Установка радиуса обводки на 50% для округления кнопки */\n"
"    width: 100px; /* Ширина кнопки */\n"
"    height: 100px; /* Высота кнопки */\n"
"}")
        self.pushButton_1_1.setFlat(False)
        self.pushButton_1_1.setObjectName("pushButton_1_1")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



        ####################################################################################
        # Buttons Actions
        self.pushButton_1_.clicked.connect(self.add_to_cart)
        self.pushButton_1_1.clicked.connect(self.add_to_cart)

        # Notifications
        self.notification = Notification('Товар успешно добавлен в корзину!')

        # Effects
        effect1 = QGraphicsDropShadowEffect(
            offset=QPoint(0, 5), blurRadius=8, color=QColor("#a2a2a2")
        )
        effect2 = QGraphicsDropShadowEffect(
            offset=QPoint(0, 5), blurRadius=8, color=QColor("#a2a2a2")
        )
        self.product_1.setGraphicsEffect(effect1)
        self.product_2.setGraphicsEffect(effect2)

    def add_to_cart(self):
        # Логика для добавления товара в корзину
        print("Товар добавлен в корзину.")  # Для отладки

        # Показать уведомление
        self.notification.show_notification()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Online Electronics Store"))
        self.label.setText(_translate("MainWindow", "Electro-NX"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_1_.setText(_translate("MainWindow", "Add to Bascket"))
        self.pushButton_1_1.setText(_translate("MainWindow", "Add to Bascket"))



# Доп. Классы
class Notification(QtWidgets.QDialog):
    def __init__(self, message):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
        self.setGeometry(600, 500, 250, 60)

        # Установка QVBoxLayout для корректного размещения метки
        layout = QtWidgets.QVBoxLayout(self)
        self.label = QtWidgets.QLabel(message)
        self.label.setStyleSheet(
            "color: white; background-color: green; padding: 10px; border-radius: 5px; font-size: 16px;")  # Установлен размер шрифта
        self.label.setWordWrap(True)
        layout.addWidget(self.label)
        self.setLayout(layout)

        # Установка позиционирования уведомления в правом нижнем углу
        screen_geometry = QtWidgets.QDesktopWidget().screenGeometry()
        self.setGeometry(screen_geometry.width() - self.width() - 20, screen_geometry.height() - self.height() - 20,
                         self.width(), self.height())


    def show_notification(self):
        self.show()
        QtCore.QTimer.singleShot(3000, self.close)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
