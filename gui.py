import tkinter as tk
from PIL import ImageTk, Image
from main import greetings
from tkinter import ttk
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import main as mn
import os


root = tk.Tk()
root.title("Kia Soul Analysis")
root.geometry("500x500")

label1 = tk.Label(root, text="Welcome to Kia Soul Analytics", pady=5, fg= 'salmon', font=('Brush Script MT', 30, 'bold'), bg='snow').place(x=50, y=50)
#label1.pack()

# image frame ============================================
frame = tk.Frame(root, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("2023_Soul.png"))

# Label Widget to display text or Image
label = tk.Label(frame, image = img)
label.pack()

#User Input =======================================================================
# this function calls the greetings() function, passes the Entry() widget
# as its parameter. get() gets whatever is in input.
def submit():
    greet = greetings(input.get())
    #label2.config(text=greet)

# Enter your name label
label3 = tk.Label(root, text="Please enter your name", pady=3, fg= 'salmon', font=('Brush Script MT', 17), bg='snow')
label3.place(x=50, y=340)
# receive entry
input = tk.Entry(root)
input.place(x=50, y=380)
#input.pack(pady=20)
# Empty label - outputs function through label - this label has nothing in it
#label2 = tk.Label(root, text="", pady=5, fg='salmon', font=('Brush Script MT', 30, 'bold'), bg='snow')
#label2 = tk.Label(root, text="", pady=5, fg= 'salmon', font=('Brush Script MT', 30, 'bold'), bg='snow')
#label2.place(x=100, y=100)
#label2.pack(pady=20)
# button to submit name and display on screen
button_user = tk.Button(root, text="Submit Input", command=submit)
button_user.place(x=60, y=410)
#button_user.pack(pady=20)



# new Window =============================================================

def open_win():
    child_win = tk.Toplevel()
    child_win.title("Soul Analytics")
    child_win.geometry("500x500")
    tk.Label(child_win, text="Kia Soul Car Sales Figures",
             fg= 'salmon', font=('Calisto MT', 14), bg='snow', pady=5).pack()

    tk.Label(child_win, text="From 2009 - 2023",
             fg='salmon', font=('Calisto MT', 14), bg='snow').pack()
    tk.Label(child_win, text="Many standard features are coherent",
             fg='salmon', font=('Calisto MT', 14), bg='snow').pack()
    #Buttons=============================================================
    tk.Button(child_win, text="Standard Features", command=d.standard_Features).place(x=75, y=140)
    tk.Button(child_win, text="2010 VS. 2022 Sales", command=t.two_Year_Sales).place(x=200, y=140)
    tk.Button(child_win, text="2014 VS. 2022 Sales", command=t.two_Year_Sales2).place(x=330, y=140)
    tk.Button(child_win, text="View Pie Chart", command=t.soul_vs_Seltos).place(x=80, y=250)
    tk.Label(child_win, text="Soul VS. Seltos Vs. Sportage in 2022?",
             fg='salmon', font=('Calisto MT', 14), bg='snow').place(x=75, y=200)




# OK button on root =====================================================
ok_Button = tk.Button(root, text="OK", command=open_win)
ok_Button.place(x=60, y=440)


# Objects of class model \\ mn is alias, main imported as mn
d = mn.model("Kia", "Soul")
print(d.company, d.model)
#d.standard_Features()

# Objects of class sales
t = mn.sales("Kia", "Soul")
#t.two_Year_Sales()
#t.two_Year_Sales2()
#t.soul_vs_Seltos()



# Get data from file
kia_Data = "kia_Soul_Sales_Figure.txt"
t.open_File(kia_Data)
raw_Data = t.open_File(kia_Data)
print(raw_Data)
#content_to_screen(c)






root.mainloop()