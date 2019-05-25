from tkinter import *
from tkinter import filedialog

class GUI():
    w=Tk()
    w.title("TXTx Application")
    w.geometry('400x200')


    def OpenFile():
        w.filename = filedialog.askopenfilename(title="Select Text X file", filetypes=(("Text X file","*.txtx"),("All files","*.*")))
        msg=tk.Message(w, text="TXT Application")
    def NewFile():
        print("Hello")
        

    menu=Menu(w)
    w.config(menu=menu)
    filemenu=Menu(menu)
    menu.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="New", command=NewFile)
    filemenu.add_command(label="Open", command=OpenFile)

    w.mainloop()
