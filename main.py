import random
from math import log, ceil
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QMessageBox, QCheckBox


class Genrator(QWidget):
    #Задание интерфейса
    def __init__(self):
        super(Genrator, self).__init__()
        self.vbox = QVBoxLayout(self)
        self.hbox_input = QHBoxLayout()
        self.hbox_button = QHBoxLayout()

        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_button)

        self.input = QLineEdit(self)
        self.hbox_input.addWidget(self.input)

        self.gen = QPushButton("generate", self)
        self.hbox_button.addWidget(self.gen)

        self.gen.clicked.connect(self._generate)

    # Функция генерации пароля
    def _generate(self):
        a = self.input.text()
        summ = 0
        t = 155
        sumg = 0
        for i in a:
            summ += ord(i)
            sumg += ord(i) ^ t
            t = (13 * t + 19) % 256
        otv = "Без граммирования: " + str(summ % 255) + "\n C граммированием: "+ str(sumg % 255)
        QMessageBox.about(self, "Контрольные суммы", otv)
        self.input.setText("")

app = QApplication(sys.argv)

win = Genrator()
win.show()

sys.exit(app.exec_())