# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 16:57:42 2023

@author: kanis
"""

from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os

root = Tk()
root.minsize(1600,1000)
root.maxsize(1000,1000)

open_img = ImageTk.PhotoImage(Image.open("open_file.png"))
save_img = ImageTk.PhotoImage(Image.open("save_file.png"))
run_img = ImageTk.PhotoImage(Image.open("run.png"))

label_file_name = Label(root, text = "File name")
label_file_name.place(relx = 0.28, rely = 0.03, anchor = CENTER)

input_file_name = Entry(root)
input_file_name.place(relx = 0.46, rely= 0.03, anchor = CENTER)

my_text = Text(root, height = 35, width = 80)
my_text.place(relx= 0.5, rely= 0.55, anchor = CENTER)

name = ""
def openFile():
    global name
    my_text.delete(1.0, END)
    text_file = filedialog.askopenfilename(title = "Open Text File",filetypes = (("Text Files", "*.txt"),))
    print(text_file)
    name = os.path.basename(text_file)
    formated_name = name.split('.')[0]
    input_file_name.insert(END, formated_name)
    root.title = (formated_name)
    text_file = open(name, 'r')
    paragraph = text_file.read()
    my_text.insert(END, paragraph)
    text_file.close()
    
def save():
    input_name = input_file_name.get()
    file = open(input_name + ".txt", "w")
    data = my_text.get("1.0", END)
    print(data)
    file.write(data)
    input_file_name.delete(0, END)
    my_text.delete(1.0, END)
    messagebox.showinfo("Updater", "Success")

def run():
    global name
    webbrowser.open(name)
      
def closeWindow():
    root.destroy()

open_button = Button(root, image=open_img, text = "OpenFile", command = openFile)
open_button.place(relx= 0.05, rely= 0.03, anchor= CENTER)

save_button = Button(root, image=save_img, text = "Save File", command=save)
save_button.place(relx=0.11, rely=0.03, anchor=CENTER)

exit_button = Button(root, text = "EXIT", command=closeWindow)
exit_button.place(relx=0.17, rely=0.03, anchor =CENTER)

run_button = Button(root, image = run_img, text = "Running", command = run)
run_button.place(relx = 0.23, rely = 0.03, anchor = CENTER)
root.mainloop()