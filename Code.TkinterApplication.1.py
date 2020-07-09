from tkinter import *

in_correct=0
correct=0

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

correct_answer = Label(logonwin, text="Sucsess", fg="green")
incorrect_answer = Label(logonwin, text="Fail, please retry", fg="red")

def checkCredentials():
    global score
    global correct
    global in_correct
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
        if in_correct == 1:
            incorrect_answer.destroy()
            in_correct = 0
            correct_answer.grid(row=5, column=5)
            correct = 1
        else:
            correct_answer.grid(row=5, column=5)
            correct = 1
    else:
        if correct == 1:
            correct_answer.destroy()
            correct = 0
            incorrect_answer.grid(row=5, column=5)
            in_correct = 1
        else:
            incorrect_answer.grid(row=5, column=5)
            in_correct = 1


userCheck = Button(logonwin, text="Logon", command=checkCredentials, font=5)
userCheck.grid(row=1, column=2)
