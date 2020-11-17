from tkinter import *
from tkinter import filedialog

class GUI():
    w=Tk()
    w.title("TXTx")
    w.geometry('400x200')

    def OpenFile():
        w.filename = filedialog.askopenfilename(title="Select Text file", filetypes=(("Text file","*.txt"),("All files","*.*")))
        msg=tk.Message(w, text="TXT Application")
        
    # Menu
    menu=Menu(w)
    w.config(menu=menu)
    filemenu=Menu(menu)
    
    ## File
    menu.add_cascade(label="File", menu=filemenu)
    ### File/Open
    filemenu.add_command(label="Open", command=OpenFile)
    
    #Makes application run forever or until close
    w.mainloop()
