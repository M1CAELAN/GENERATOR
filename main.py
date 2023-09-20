import random
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QMessageBox


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
        log = self.input.text()
        pasw = ''
        while True:
            for i in range(3):
                    pasw = pasw + chr(random.randint(ord('a'), ord('z')))
            for i in range(2):
                pasw = pasw + chr(random.randint(ord('A'), ord('Z')))
            pasw = pasw + str((len(log)**4)%100)
            if len(pasw) < 7:
                a = pasw[5]
                pasw = pasw[:5]
                pasw = pasw + "0" + a
            if pasw != log:
                break
        QMessageBox.about(self, "Ваш пароль", pasw)
        self.input.setText("")

app = QApplication(sys.argv)

win = Genrator()
win.show()

sys.exit(app.exec_())