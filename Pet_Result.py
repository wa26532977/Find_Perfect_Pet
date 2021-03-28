from PyQt5 import QtWidgets
import sys
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
import os
import pandas as pd


class ResultShow(QDialog):
    def __init__(self, answer=None, dog_name_1=None, other_dog=None):
        super(ResultShow, self).__init__()
        loadUi("UI_Files\\Result.ui", self)
        self.answer = answer
        self.dog_name_1 = dog_name_1
        self.other_dog = other_dog
        self.setup_page()
        self.user_input_database_path = os.path.dirname(sys.argv[0]) + r"\\Pet_DataBase\\user_input_database.txt"
        self.pushButton.clicked.connect(self.user_suggestion)

    def setup_page(self):
        self.label_2.setText(self.dog_name_1)
        if self.other_dog != '':
            self.label_4.setText("Other suitable dog " + self.other_dog[:-2])

    def user_suggestion(self):
        user_input = self.lineEdit.text()
        print(user_input)

        data_file = pd.read_csv(self.user_input_database_path, sep="\t")
        answer_count = data_file["answer"].last_valid_index()
        if answer_count is None:
            answer_count = 0
        else:
            answer_count += 1

        data_file.loc[answer_count] = [str(self.answer), user_input]
        data_file.to_csv(self.user_input_database_path, sep="\t", index=False)
        msgbox = QtWidgets.QMessageBox(self)
        msgbox.setText("Your input is submitted. Thank you!")
        msgbox.exec()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    qt_app = ResultShow(answer=[1, 2, 3, 4, 5], dog_name_1="Very Good Dog", other_dog="happy1, happy2, happy3, ")
    qt_app.show()
    app.exec_()