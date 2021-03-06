from PyQt5 import QtWidgets
import sys
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
import os


class QuestionWithFunction(QDialog):
    def __init__(self):
        super(QuestionWithFunction, self).__init__()
        loadUi("UI_Files\\QuestionAsk.ui", self)
        # self.pushButton.clicked.connect(self.start_button)
        self.question = {'Where will you new dog live?': ['Apartment', 'House'],
                         'How much space will he has to play?':
                             ['No outdoor space', 'Small Yard', 'Average Yard', 'Large Yard', 'Acreage'],
                         'Will he have any kids to snuggle with?':
                             ["No, I don't have kids and I'm not planning on it", "No, I don't have kids yet",
                              "Yes, I have kids under 12 years old", "Yes, I have kids over 12 years old"],
                         "Have you owned A dog before?": ["I'm an experienced dog owner", 'This will be my first dog'],
                         "Will he have roommates? (Other pets)":
                             ["No other pets", "Other dogs", "Cats", "other small animals"],
                         "Which best describes your future pet’s personality?":
                             ["Highly protective", "Moderately protective", "Fairly Friendly with strangers",
                              "Loves everyone"],
                         "In terms of barking, how much noise can you tolerate?":
                             ["None, I prefer a dog who doesn't bark much", "Some barking doesn't bother me too much",
                              "Barking is not an issue for me"],
                         "How much will your dog be able to play with you?":
                             ["Only indoor playtime", "A short walk or backyard play", "Occasional long walks",
                              "Daily walks and jogs"],
                         "How much time will your new dog be spending alone?":
                             ["I or someone else will be home most of the time", "Only about 4 hours at a time",
                              "Just until I get home from work",
                              "My dog should be fine by himself for at least 8 hours"],
                         "How much training will your new dog receive?": ["None", "Basic obedience",
                                                                          "Advanced obedience"],
                         "How big or small will your new dog be?": ["15 LB and under", "15-30 LB", "30-50 LB",
                                                                    "50-100 LB",
                                                                    "110 LB and over", "No preference"],
                         "How much time can you dedicate to your new dog's grooming?": ["Very little", "Every so often",
                                                                                        'Daily'],
                         "How important is having a dog that doesn't shed much?":
                             ["I prefer dog with minial shedding", "A little shedding is ok", "Not important"]
                         }


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    qt_app = QuestionWithFunction()
    qt_app.show()
    app.exec_()
