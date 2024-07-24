from tkinter import *
import random
import string
import pyperclip

def copy_password():
    pyperclip.copy(pass_prt.get())

def clear():
    pass_prt.set('')
    pass_len.set('')

def generator():
    password = ''
    if int(pass_len.get()) < 5:
        pass_prt.set('TOO SHORT!')
        return
    elif int(pass_len.get()) > 21:
        pass_prt.set('TOO LONG!')
        return
    password = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.digits) + random.choice(string.punctuation)
    for _ in range(int(pass_len.get()) - 4):
        password += random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_prt.set(password)

root = Tk()
root.geometry("600x600")
root.resizable(0, 0)
root.title("PASSWORD GENERATOR")

img = PhotoImage(file="C:/Users/Raman Sharma/OneDrive/Desktop/py/pass.png")
l = Label(root, image=img)
l.place(relheight=1, relwidth=1)

h = Label(l, text='PASSWORD GENERATOR', bg='white', font='arial 15 bold', height=2, width=30)
h.pack(pady=5)

Label(l, text='RPG', font='arial 15 bold').pack(side=BOTTOM)

pass_label = Label(l, text='PASSWORD LENGTH', font='arial 12 bold', height=2, width=30)
pass_label.pack(pady=10)

pass_len = StringVar()
length = Entry(l, textvariable=pass_len, width=15)
length.pack()

pass_prt = StringVar()

Button(l, text="GENERATE PASSWORD", font='arial 10 bold', command=generator).pack(pady=5)
Entry(l, textvariable=pass_prt).pack()

Button(l, text='COPY TO CLIPBOARD', command=copy_password).pack(pady=10)
Button(l, text='CLEAR', command=clear).pack(pady=5)

root.mainloop()
