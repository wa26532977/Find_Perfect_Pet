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

    def start_button(self):
        ui = QuestionWithFunction.QuestionWithFunction()
        self.close()
        ui.show()
        ui.exec_()

    # import ast
    # import requests
    # dic_str = requests.get(r"https://dog.ceo/api/breed/akita/images/random").content.decode("UTF-8")
    # my_data = ast.literal_eval(dic_str)
    # if my_data["status"] == "success":
    #     pic_URL = my_data["message"].replace('\\', '')
    #     print(type(my_data))
    #     img_get = requests.get(pic_URL).content
    #     with open('image_name.jpg', 'wb') as handler:
    #         handler.write(img_get)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    qt_app = FindPetApp()
    qt_app.show()
    app.exec_()