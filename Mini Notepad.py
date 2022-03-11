from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
import os

root = Tk()
root.title("Mini Notepad")
root.maxsize(650,650)
root.minsize(650,650)

open_img = ImageTk.PhotoImage(Image.open("open.png"))
save_img = ImageTk.PhotoImage(Image.open("save.png"))
close_img = ImageTk.PhotoImage(Image.open("exit.jpg"))

label_filename = Label(root, text = "File Name: ")
label_filename.place(relx=0.28,rely=0.03, anchor = CENTER)

input_filename = Entry(root)
input_filename.place(relx=0.46,rely=0.03,anchor=CENTER)

my_text = Text(root, height=35, width=80)
my_text.place(relx=0.5,rely=0.55,anchor=CENTER)

name = ""

def openFile():
    global name
    my_text.delete(1.0, END)
    input_filename.delete(0, END)
    text_file = filedialog.askopenfilename(title="Open Text File",filetypes=(("Text Files","*.txt"),))
    print(text_file)
    name = os.path.basename(text_file)
    formatted_name = name.split('.')[0]
    input_filename.insert(END, formatted_name)
    root.title(formatted_name)
    text_file = open(name, 'r')
    paragraph = text_file.read()
    my_text.insert(END, paragraph)
    text_file.close()
    
def saveFile():
    input_name = input_filename.get()
    file = open(input_name+".txt", "w")
    data = my_text.get("1.0", END)
    print(data)
    file.write(data)
    input_filename.delete(0,END)
    my_text.delete(1.0,END)
    messagebox.showinfo("Success","Success")
    
def closeFile():
    root.destroy()
    
open_button = Button(root, image = open_img, text = "Open File", command = openFile)
open_button.place(relx=0.05,rely=0.03,anchor=CENTER)

save_button = Button(root, image = save_img, text = "Save File", command = saveFile)
save_button.place(relx=0.11,rely=0.03,anchor=CENTER)

close_button = Button(root, image = close_img, text = "Close File", command = closeFile)
close_button.place(relx=0.17,rely=0.03,anchor=CENTER)

root.mainloop()