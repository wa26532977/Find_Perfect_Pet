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
import pandas as pd
import Pet_Result

pd.options.display.max_columns = 999
pd.options.display.max_rows = 999
pd.set_option("display.precision", 6)


class QuestionWithFunction(QDialog):
    def __init__(self):
        super(QuestionWithFunction, self).__init__()
        loadUi("UI_Files\\QuestionAsk.ui", self)
        self.pushButton.clicked.connect(self.next_question)
        self.pushButton_2.clicked.connect(self.back_button)
        self.data_path = os.path.dirname(sys.argv[0]) + r"\\Pet_DataBase\\find_pet_database.txt"
        self.data_file = pd.read_csv(self.data_path, sep="\t")
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

    def back_button(self):
        self.q_number -= 1
        ui = QuestionWithFunction()
        ui.display(q_number=self.q_number, answer=self.answer)
        self.close()
        ui.show()
        ui.exec_()

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
        for i in range(len(self.questions[self.q_number][1])):
            run_line = f"self.radioButton_{i}.isChecked()"
            if eval(run_line):
                # for back button this will make sure the array is accurate
                if len(self.answer) > self.q_number:
                    self.answer[self.q_number] = i
                else:
                    self.answer.append(i)
                self.q_number += 1
                print(f"q_number = {self.q_number}, answer = {self.answer}")
                # this is end of the question, so we will run the query for the result
                if self.q_number == 5:
                    print("find the right pet")

                    only_once = True
                    other_dog = ""
                    dog_name_1 = ''
                    for item in self.data_file[self.data_file["answer"] == str(self.answer)]['dog_name']:
                        if only_once:
                            only_once = False
                            dic_str = requests.get(r"https://dog.ceo/api/breed/" + item + "/images/random").content.decode("UTF-8")
                            pic_data = ast.literal_eval(dic_str)
                            if pic_data["status"] == "success":
                                pic_URL = pic_data["message"].replace('\\', '')
                                print(pic_data)
                                img_get = requests.get(pic_URL).content
                                with open('Images/found_prefect_pet.jpg', 'wb') as handler:
                                    handler.write(img_get)
                                dog_all_name = pic_URL[30:]
                                dog_name_1 = dog_all_name[:dog_all_name.find("/")]
                                if '-' in dog_name_1:
                                    dog_name_1_list = dog_name_1.split('-')
                                    dog_name_1 = dog_name_1_list[1].capitalize() + " " + dog_name_1_list[0].capitalize()
                                    print(dog_name_1)
                        else:
                            other_dog += item + ", "

                    ui = Pet_Result.ResultShow(answer=self.answer, dog_name_1=dog_name_1, other_dog=other_dog)
                    self.close()
                    ui.show()
                    ui.exec_()
                    return

                ui = QuestionWithFunction()
                ui.display(q_number=self.q_number, answer=self.answer)
                self.close()
                ui.show()
                ui.exec_()
                return
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
