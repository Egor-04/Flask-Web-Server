from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
import sys


class Notification(QtWidgets.QDialog):
    def __init__(self, message, position_counter, notification_manager):
        super().__init__()

        # Установка флагов окна
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)

        # Установка размеров уведомления
        self.setFixedSize(250, 60)

        # Установка метки
        self.label = QtWidgets.QLabel(message)
        self.label.setStyleSheet(
            "color: white; background-color: green; padding: 10px; border-radius: 5px; font-size: 16px;")
        self.label.setWordWrap(True)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.label)
        self.setLayout(layout)

        # Установка начального положения уведомления
        screen_geometry = QtWidgets.QDesktopWidget().screenGeometry()
        self.setGeometry(screen_geometry.width() - 270, screen_geometry.height() - (position_counter * 70) - 70,
                         self.width(), self.height())

        # Анимация всплытия
        self.animation = QtCore.QPropertyAnimation(self, b"pos")
        self.animation.setDuration(500)
        self.animation.setStartValue(QPoint(screen_geometry.width() - self.width() - 20, screen_geometry.height()))
        self.animation.setEndValue(QPoint(screen_geometry.width() - self.width() - 20,
                                          screen_geometry.height() - (position_counter * 70) - 70))

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


class Ui_MainWindow:
    def __init__(self):
        self.notification_count = 0  # Счетчик уведомлений

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)

        # Центральный виджет
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

        # Создание главного макета
        main_layout = QtWidgets.QVBoxLayout(self.centralwidget)

        # Кнопки
        self.pushButton_1_ = QtWidgets.QPushButton("Добавить товар 1", self.centralwidget)
        self.pushButton_1_1 = QtWidgets.QPushButton("Добавить товар 2", self.centralwidget)

        main_layout.addWidget(self.pushButton_1_)
        main_layout.addWidget(self.pushButton_1_1)

        # Подключение кнопок к действиям
        self.pushButton_1_.clicked.connect(self.add_to_cart)
        self.pushButton_1_1.clicked.connect(self.add_to_cart)

        # Эффекты для кнопок
        effect1 = QGraphicsDropShadowEffect(offset=QPoint(0, 5), blurRadius=8, color=QColor("#a2a2a2"))
        effect2 = QGraphicsDropShadowEffect(offset=QPoint(0, 5), blurRadius=8, color=QColor("#a2a2a2"))
        self.pushButton_1_.setGraphicsEffect(effect1)
        self.pushButton_1_1.setGraphicsEffect(effect2)

    def add_to_cart(self):
        self.notification_count += 1  # Увеличиваем счетчик уведомлений
        message = 'Товар успешно добавлен в корзину!'
        notification = Notification(message, self.notification_count, self)
        notification.show_notification()

    def decrement_counter(self):
        self.notification_count -= 1  # Уменьшаем счетчик уведомлений


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
