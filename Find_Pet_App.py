from PyQt5 import QtWidgets
import sys
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
import QuestionWithFunction
import os


class FindPetApp(QDialog):
    def __init__(self):
        super(FindPetApp, self).__init__()
        loadUi("UI_Files\\Start_Window.ui", self)
        self.label_2.setPixmap(QPixmap(os.getcwd() + r"\Images\golden_retriever_puppies.jpg"))
        self.pushButton.clicked.connect(self.start_button)

    def start_button(self):
        ui = QuestionWithFunction.QuestionWithFunction()
        ui.display(q_number=0, answer=[])
        self.close()
        ui.show()
        ui.exec_()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    qt_app = FindPetApp()
    qt_app.show()
    app.exec_()