from tkinter import *
from tkinter import filedialog

class GUI():
    w=Tk()
    w.title("TXT file open Application")
    w.geometry('400x200')


    def OpenFile():
        w.filename = filedialog.askopenfilename(title="Select Text file", filetypes=(("Text file","*.txt"),("All files","*.*")))
        msg=tk.Message(w, text="TXT Application")
        

    menu=Menu(w)
    w.config(menu=menu)
    filemenu=Menu(menu)
    menu.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="Open", command=OpenFile)

    w.mainloop()
