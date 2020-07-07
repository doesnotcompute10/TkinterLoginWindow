from tkinter import *
import random

logonwin = Tk()
username="travisje26"
password="pythonissohard10"

usernameInn = Entry(logonwin, width=50)
usernameInn.grid(row=1, column=0)

usernameAnn = Label(logonwin, text="Username:")
usernameAnn.grid(row=0, column=0)

passwordInn = Entry(logonwin, width=50)
passwordInn.grid(row=1, column=1)

passwordAnn = Label(logonwin, text="Password:")
passwordAnn.grid(row=0, column=1)

def checkCredentials():
    global score
    score = 0
    usernameIn = usernameInn.get()
    passwordIn = passwordInn.get()

    if usernameIn == username:
        score = score+1
    else:
        print(" ")

    if passwordIn == password:
        score = score+1
    else:
        print(" ")

    if score == 2:
        print("Activated")
    else:
        print("Fail, please try again later")

userCheck = Button(logonwin, text="Logon", command=checkCredentials)
userCheck.grid(row=1, column=2)

## ABOVE IS NOT TO BE EDITED ##
