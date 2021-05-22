from tkinter import Button, Tk, Frame, Label, Button
from time import sleep
from tkinter import font
from tkinter.constants import LEFT, TOP
from tkinter.font import BOLD

class Question:
    def __init__(self, question, answers, correctLetter):
        self.question = question
        self.answers = answers
        self.correctLetter = correctLetter

    def check(self, letter, view):
        global right
        if(letter == self.correctLetter):
            label = Label(view,font=("Georgia",20,BOLD),text="Right!-You WIN 2000rs")
            right += 1
        else:
            label = Label(view,font=("Georgia",20,BOLD), text="Wrong!-You LOSS 2000rs")
            # window.destroy()
        label.pack()
        view.after(1000, lambda *args: self.unpackView(view))


    def getView(self, window):
        view = Frame(window)
        l1 = Label(view,font=("Georgia",20,BOLD),text=self.question).pack()
        Button(view,font=("Georgia",20,BOLD), text=self.answers[0], command=lambda *args: self.check("A", view),fg="blue").pack(side=LEFT)
        Button(view,font=("Georgia",20,BOLD), text=self.answers[1], command=lambda *args: self.check("B", view),fg="blue").pack(side=LEFT)
        Button(view,font=("Georgia",20,BOLD), text=self.answers[2], command=lambda *args: self.check("C", view),fg="blue").pack(side=LEFT)
        Button(view,font=("Georgia",20,BOLD),text=self.answers[3], command=lambda *args: self.check("D", view),fg="blue").pack(side=LEFT)
        # btn = Button(window, text = "click me !", bd = "5", command = window.destroy)
        # btn.pack(side = "top")
        return view

    def unpackView(self, view):
        view.pack_forget()
        askQuestion()

def askQuestion():
    global questions, window, index, button, right, number_of_questions 
    if(len(questions) ==index + 1):
        Label(window,font=("Georgia",20,BOLD),text="Thank you for answering the questions. ").pack()
        return
    button.pack_forget()
    index += 1
    questions[index].getView(window).pack()

questions = []
file = open("questions.txt", "r")
line = file.readline()
while(line != ""):
    questionString = line
    answers = []
    for i in range (4):
        answers.append(file.readline())

    correctLetter = file.readline()
    correctLetter = correctLetter[:-1]
    questions.append(Question(questionString, answers, correctLetter))
    line = file.readline()
file.close()
index = -1
right = 0
number_of_questions = len(questions)
window = Tk()
label = Label(window,font=("Georgia",30,BOLD),text="Welcome to kbc Game",bg="blue",fg="white")
label.pack()
window.title("kon banega karodapati")
window.config(background="black")
from tkinter import*
from random import randint
img = PhotoImage(file="/home/gauri/Downloads/KBC.png")
image_list = [img]
pick_number = randint(0,0)
image_label =  Label(image = image_list[pick_number])
image_label.pack(pady = 20)
button = Button(window,font=("Georgia",20,BOLD),bd=10,height=2,width=6,text="Start",fg="blue", command=askQuestion)
button.pack()
window.mainloop()
