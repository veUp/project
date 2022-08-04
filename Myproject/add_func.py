from tkinter import *
from tkinter import messagebox as mb
import time
import account

class Window_add:
    def __init__(self,parent):
        self.root = Toplevel(parent)
        self.root.title('Запись веса')
        self.root.iconbitmap('ico.ico')
        self.root.configure(bg='#f3f76a')
        self.flg_exit = False
        self.mass = Entry(self.root)

    def focus(self):
        self.root.grab_set()
        self.root.focus_set()
        self.root.wait_window()

    def draw_widgest(self):
        color = '#f3f76a'
        Label(self.root,text='Ваш вес',justify=CENTER,bg=color,font=16).grid(row=1,column=0,sticky=W,pady=10,padx=10)
        self.mass.grid(row=1,column=1,sticky=W+E,padx=10)
        Button(self.root,text='Сохранить',justify=CENTER,bg=color,command=self.save_data).grid(row=3,column=0,sticky=W,padx=10,pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.exit)
        self.focus()

    def exit(self):
        self.root.destroy()
        self.flg_exit=True

    def run(self, login=None):
        self.login = login
        self.draw_widgest()
        if self.flg_exit:
            return self.flg_exit
        self.root.mainloop()

    def save_data(self):
        t = time.localtime()
        self.time = [t.tm_mday,t.tm_mon,t.tm_year]
        mass =self.mass.get()

        start = account.Mass_user(self.login,mass,self.time)
        start.add_mass()
