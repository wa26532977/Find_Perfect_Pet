from PyQt5 import QtWidgets
import sys
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
import os
import ast
import requests
import random
from os import listdir
from os.path import isfile, join


class QuestionWithFunction(QDialog):
    def __init__(self):
        super(QuestionWithFunction, self).__init__()
        loadUi("UI_Files\\QuestionAsk.ui", self)
        self.pushButton.clicked.connect(self.next_question)
        self.answer = []
        self.q_number = 0
        self.questions = [('Where will you new dog live?', ['Apartment', 'House']),
                          ('How much space will he has to play?', ['No outdoor space', 'Small Yard',
                                                                   'Average Yard', 'Large Yard', 'Acreage']),
                          ('Will he have any kids to snuggle with?',
                           ["No, I don't have kids and I'm not planning on it", "No, I don't have kids yet",
                            "Yes, I have kids under 12 years old", "Yes, I have kids over 12 years old"]),
                          ("Have you owned A dog before?",
                           ["I'm an experienced dog owner", 'This will be my first dog']),
                          ("Will he have roommates? (Other pets)",
                           ["No other pets", "Other dogs", "Cats", "other small animals"]),
                          ("Which best describes your future pet’s personality?",
                           ["Highly protective", "Moderately protective", "Fairly Friendly with strangers",
                            "Loves everyone"]),
                          ("In terms of barking, how much noise can you tolerate?",
                           ["None, I prefer a dog who doesn't bark much", "Some barking doesn't bother me too much",
                            "Barking is not an issue for me"]),
                          ("How much will your dog be able to play with you?",
                           ["Only indoor playtime", "A short walk or backyard play", "Occasional long walks",
                            "Daily walks and jogs"]),
                          ("How much time will your new dog be spending alone?",
                           ["I or someone else will be home most of the time", "Only about 4 hours at a time",
                            "Just until I get home from work",
                            "My dog should be fine by himself for at least 8 hours"]),
                          ("How much training will your new dog receive?",
                           ["None", "Basic obedience", "Advanced obedience"]),
                          ("How big or small will your new dog be?",
                           ["15 LB and under", "15-30 LB", "30-50 LB", "50-100 LB",
                            "110 LB and over", "No preference"]),
                          ("How much time can you dedicate to your new dog's grooming?",
                           ["Very little", "Every so often", 'Daily']),
                          ("How important is having a dog that doesn't shed much?",
                           ["I prefer dog with minial shedding", "A little shedding is ok", "Not important"])]

    def display(self, q_number, answer):
        self.answer = answer
        self.q_number = q_number
        self.label.setText(self.questions[q_number][0])
        for i in range(len(self.questions[q_number][1])):
            run_line = f"self.radioButton_{i}.setText(self.questions[q_number][1][i])"
            exec(run_line)

        for i in range(len(self.questions[q_number][1]), 6):
            run_line = f"self.radioButton_{i}.setHidden(True)"
            exec(run_line)

        my_path = os.getcwd() + r"\Images\\"
        only_files = [f for f in listdir(my_path) if isfile(join(my_path, f))]
        self.label_2.setPixmap(QPixmap(my_path + only_files[random.randrange(len(only_files))]))

    def next_question(self):
        if self.questions == 13:
            print("do the query and find the dog")

        for i in range(len(self.questions[self.q_number][1])):
            run_line = f"self.radioButton_{i}.isChecked()"
            if eval(run_line):
                self.answer.append(i)
                self.q_number += 1
                print(f"q_number = {self.q_number}, answer = {self.answer}")
                ui = QuestionWithFunction()
                ui.display(q_number=self.q_number, answer=self.answer)
                self.close()
                ui.show()
                ui.exec_()
                break
            # if nothing is checked
        msgbox = QtWidgets.QMessageBox(self)
        msgbox.setText("No item is selected, please select an item.")
        msgbox.exec()
        return


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    qt_app = QuestionWithFunction()
    qt_app.show()
    app.exec_()
