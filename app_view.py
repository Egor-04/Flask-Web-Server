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
        self.scrollArea.setGeometry(QtCore.QRect(10, 110, 1371, 921))
        self.scrollArea.setAcceptDrops(False)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1352, 919))
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
        self.label_13.setPixmap(QtGui.QPixmap("../Online_Electronics_Store/Images/Monitor.jpg"))
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
        self.label_14.setPixmap(QtGui.QPixmap("../Online_Electronics_Store/Images/Monitor.jpg"))
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Online Electronics Store"))
        self.label.setText(_translate("MainWindow", "Electro-NX"))
        self.pushButton_1_.setText(_translate("MainWindow", "Add to Bascket"))
        self.pushButton_1_1.setText(_translate("MainWindow", "Add to Bascket"))




####################################################################################
        # Количество уведомлений
        self.notification_count = 0

        #Buttons Actions
        self.pushButton_1_.clicked.connect(self.add_to_cart)
        self.pushButton_1_1.clicked.connect(self.add_to_cart)

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
        self.notification_count += 1  # Увеличиваем счетчик уведомлений
        message = 'Товар успешно добавлен в корзину!'
        notification = Notification(message, self.notification_count, self)
        notification.show_notification()

    def decrement_counter(self):
        self.notification_count = 0  # Уменьшаем счетчик уведомлений



# Доп. Классы
class Notification(QtWidgets.QDialog):
#Надо создать один VBox и использовать его для отслеживания количества сообщений внутри и удалять их

    def __init__(self, message, notification_count, notification_manager):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)

        # Установка размеров уведомления
        self.setGeometry(600, 500 + (notification_count * 70), 250, 60)

        # Установка QVBoxLayout для корректного размещения метки
        layout = QtWidgets.QVBoxLayout(self)
        self.label = QtWidgets.QLabel(message)
        self.label.setStyleSheet(
            "color: white; background-color: green; padding: 10px; border-radius: 5px; font-size: 16px;")
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
        self.timer.start(4000)  # 4 секунды


    def remove_notification(self, notification_manager):
        notification_manager.decrement_counter()  # Обновляем счетчик в менеджере уведомлений.
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
