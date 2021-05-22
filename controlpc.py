from tkinter import *
import os

def shutdown():
    return os.system('shutdown /s /t 1')

def restart():
    return os.system('shutdown /r /t 1')

def logout():
    return os.system('shutdown -1')

master=Tk()
master.configure(bg='light blue')
Button(master,text='Shutdown',command=shutdown).place(x=20,y=20)
Button(master,text='Restart',command=restart).restart(x=25,y=50)
Button(master,text='Log out',command=logout).logout(x=20,y=80)

mainloop()