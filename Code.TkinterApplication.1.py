from tkinter import *

logonwin = Tk()
username = "github_online_repo"
password = "pythonissohard10"

username_inn = Entry(logonwin, width=50)
username_inn.grid(row=1, column=0)

usernameAnn = Label(logonwin, text="Username:")
usernameAnn.grid(row=0, column=0)

passwordInn = Entry(logonwin, width=50)
passwordInn.grid(row=1, column=1)

passwordAnn = Label(logonwin, text="Password:")
passwordAnn.grid(row=0, column=1)


def checkCredentials():
    global score
    score = 0
    username_in = username_inn.get()
    passwordIn = password_inn.get()

    if username_in == username:
        score = score + 1
    else:
        print(" ")

    if password_in == password:
        score = score + 1
    else:
        print(" ")

    if score == 2:
        print("Activated")
    else:
        print("Fail, please try again later")


userCheck = Button(logonwin, text="Logon", command=checkCredentials)
userCheck.grid(row=1, column=2)

## ABOVE IS NOT TO BE EDITED ##
