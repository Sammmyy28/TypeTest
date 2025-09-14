import tkinter as tk
import time
import threading
import random
from tkinter import *

# create a class for ul elements
class TypingTest:

    # create a simple constructor
    def __init__(test):
        test.root = tk.Tk()
        test.root.title("Typing Speed Tester")
        test.root.geometry("1550x890")

        bg = PhotoImage(file="bg1.png")
        myLabel=Label(test.root,image=bg)
        myLabel.place(x=0,y=0,relwidth=1,relheight=1)
        
        test.text = open("easy_text.txt", "r").read().split("\n")

        test.frame = tk.Frame(test.root)
        bg2 = PhotoImage(file="bg1.png")
        mylabel=Label(test.frame,image=bg2)
        mylabel.place(x=0,y=0,relwidth=1,relheight=1)

        test.T = tk.Label(test.frame, text="EASY", font=("Helventica", 28))
        test.T.grid(row=0, column=0, columnspan=2, padx=5, pady=10)

        # creating a lable
        test.choice = random.choice(test.text)
        test.sample_label = tk.Label(test.frame, text=test.choice, font=("Helventica", 24))
        test.sample_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
                
        
        # creating a text box
        test.input_entry = tk.Entry(test.frame, width=40, font=("Helventica", 36))
        test.input_entry.grid(row=2, column=0, columnspan=2, padx=5, pady=10)
        # adding the function to start automatically if the key is pressed
        test.input_entry.bind("<KeyPress>", test.start)    

        # creating a label for the timer
        test.speed_label = tk.Label(test.frame, text="Speed:\n0.00 CPM\n0.00 WPM\n0.00 secs", font=("jokerman", 28))
        test.speed_label.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

        # creating a reset button
        test.reset_button = tk.Button(test.frame, text="Refresh", command=test.reset, font=("Helventica", 24))
        test.reset_button.grid(row=5, column=0, columnspan=2, padx=5, pady=10)

        test.frame.pack(expand=True)


        # adding the boolean to know that the app is started or not
        test.counter = 0
        test.running = False

        test.root.mainloop()

    def start(test, event):
        if not test.running:
            test.running = True
            t = threading.Thread(target=test.time_thread)
            t.start()
        if not test.sample_label.cget('text').startswith(test.input_entry.get()):
            test.input_entry.config(fg="red")
        else:
            test.input_entry.config(fg="black")
        if test.input_entry.get() == test.sample_label.cget('text')[:-1]:
            test.running = False
            test.input_entry.config(fg="green")


    def time_thread(test):
        while test.running:
            time.sleep(0.1)
            test.counter += 0.1
            cpm = (len(test.input_entry.get()) / test.counter) * 60
            wpm = (len(test.input_entry.get().split()) / test.counter) * 60
            secs = test.counter
            test.speed_label.config(text=f"Speed:\n{cpm:.2f} CPM\n{wpm:.2f} WPM\n{secs:.2f} secs")
                    

    def reset(test):
        test.running = False
        test.counter = 0
        test.speed_label.config(text="Speed:\n0.00 CPM\n0.00 WPM\n 0.00 secs")
        test.sample_label.config(text=random.choice(test.text))
        test.input_entry.delete(0, tk.END)

TypingTest()

