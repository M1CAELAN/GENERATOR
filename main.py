import random
from math import log, ceil
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QMessageBox, QCheckBox


class Genrator(QWidget):
    #Задание интерфейса
    def __init__(self):
        super(Genrator, self).__init__()
        self.vbox = QVBoxLayout(self)
        self.hbox_button = QHBoxLayout()
        self.hbox_checkbox = QHBoxLayout()
        self.hbox_checkbox1 = QHBoxLayout()
        self.hbox_checkbox2 = QHBoxLayout()

        self.vbox.addLayout(self.hbox_checkbox)
        self.vbox.addLayout(self.hbox_checkbox1)
        self.vbox.addLayout(self.hbox_checkbox2)
        self.vbox.addLayout(self.hbox_button)

        self.gen = QPushButton("generate", self)
        self.hbox_button.addWidget(self.gen)

        self.checkbox = QCheckBox('англиские строчные', self)
        self.hbox_checkbox.addWidget(self.checkbox)
        self.checkbox1 = QCheckBox('англиские прописные', self)
        self.hbox_checkbox1.addWidget(self.checkbox1)
        self.checkbox2 = QCheckBox('цифры', self)
        self.hbox_checkbox2.addWidget(self.checkbox2)

        self.gen.clicked.connect(self._generate)

    # Функция генерации пароля
    def _generate(self):
        bord = 4320000000
        pasw = ''
        dict = ""
        if self.checkbox.isChecked():
            dict = dict + "qwertyuiopasdfghjklzxcvbn"
        if self.checkbox1.isChecked():
            dict = dict + "QWERTYUIOPASDFGHJKLZXCVBNM"
        if self.checkbox2.isChecked():
            dict = dict + "0123456789"
        if len(dict) == 0:
            QMessageBox.about(self, "Ошибка", "Не указаны возможные символы")
        else:
            lenn = ceil(log(bord, len(dict)))
            for i in range(lenn):
                pasw = pasw + dict[random.randint(0, len(dict)-1)]
            QMessageBox.about(self, "Ваш пароль", pasw)

app = QApplication(sys.argv)

win = Genrator()
win.show()

sys.exit(app.exec_())