from tkinter import *

logonwin = Tk()
username = "github_online_repo"
password = "pythonissohard10"

username_inn = Entry(logonwin, width=50, font=5)
username_inn.grid(row=1, column=0)

username_ann = Label(logonwin, text="Username:", font=5)
username_ann.grid(row=0, column=0)

password_inn = Entry(logonwin, width=50, show="*", font=5)
password_inn.grid(row=1, column=1)

password_ann = Label(logonwin, text="Password:", font=5)
password_ann.grid(row=0, column=1)


def checkCredentials():
    global score
    score = 0

    if username_inn.get() == username:
        score = score + 1
    else:
        print(" ")

    if password_inn.get() == password:
        score = score + 1
    else:
        print(" ")

    if score == 2:
        print("Activated")
    else:
        print("Fail, please retry")


userCheck = Button(logonwin, text="Logon", command=checkCredentials, font=5)
userCheck.grid(row=1, column=2)

