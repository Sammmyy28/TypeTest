from tkinter import *
import tkinter as tk
import os

a = Tk()

a.geometry("1550x890")
a.title("Typing Test")

def easy():
    easy = os.system("easy.py")
def medium():
    medium = os.system("medium.py")
def hard():
    hard = os.system("hard.py")

bg = PhotoImage(file="woodnew.png")
label=Label(a,image=bg)
label.place(x=0,y=0,relwidth=1,relheight=1)

T = tk.Label(a, text="WELCOME TO THE TYPING TEST", font=("Helventica", 30))
T.grid(row=0, column=0, columnspan=2, padx=5, pady=10)
T.place(x=430,y=80)
T1 = tk.Label(a, text="Please choose your difficulty...", font=("Helventica", 28))
T1.grid(row=1, column=0, columnspan=2, padx=5, pady=10)
T1.place(x=500,y=150)

b1 = Button(a,text = "EASY",command = easy,font=("Helvetica", 18),activeforeground = "green",activebackground = "white",padx=15,pady=20)
b1.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
b1.place(x=700, y=350)
b2 = Button(a,text = "MEDIUM",command = medium,font=("Helvetica", 18),activeforeground = "orange",activebackground = "white",padx=15,pady=20)
b2.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
b2.place(x=685, y=450)
b3 = Button(a,text = "HARD",command = hard,font=("Helvetica", 18),activeforeground = "red",activebackground = "white",padx=15,pady=20)
b3.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
b3.place(x=700, y=550)

a.mainloop()


