from tkinter import *
from tkinter import messagebox as mb
import account
import add_func
class Window:
    def __init__(self,parent):
        self.root = Toplevel(parent)
        self.root.geometry('300x300+600+300')
        self.root.iconbitmap('ico.ico')
        self.root.configure(bg='#f3f76a')
        self.flg_exit = False



    def draw_widgest(self):
        Button(self.root, text='Запись веса', justify=CENTER, bg='#fcca72', command=self.add_mass,font=16).pack(pady=20)
        Button(self.root, text='Показать историю', justify=CENTER, bg='#fcca72', command=self.show_history,font=16).pack(pady=20)
        Button(self.root, text='Выход в главное меню', justify=CENTER, bg='#fcca72', command=self.exit,font=16).pack(pady=20)
        self.root.protocol("WM_DELETE_WINDOW",self.exit)
        self.focus()
    def exit(self):
        self.flg_exit = True
        self.root.destroy()

    def add_mass(self):
        start = add_func.Window_add(self.root)
        self.root.withdraw()
        i = start.run(self.login)
        if i:
            self.root.deiconify()

    def show_history(self):
        start = account.Mass_user(self.login)
        a = start.show_history()
        if start is not False:
            ab = CrollBarWindow(self.root,a)
            self.root.withdraw()
            flg = ab.run()
            if flg:
                self.root.deiconify()
        else:
            mb.showwarning('Ошибка','История пуста!')

    def run(self,login=None):
        self.login = login
        self.draw_widgest()
        if self.flg_exit:
            return self.flg_exit
        self.root.mainloop()

    def focus(self):
        self.root.grab_set()
        self.root.focus_set()
        self.root.wait_window()

class CrollBarWindow:
    def __init__(self,parent,data):
        self.root = Toplevel(parent)
        self.root.iconbitmap('ico.ico')
        self.root.configure(bg='#f3f76a')
        self.flg_exit = False
        self.data = data

    def drow_widgest(self):
        Label(self.root,text='История изменения веса',bg='#f3f76a',font=16,justify=CENTER).pack(pady=10)
        for x in self.data:
            Label(self.root,text=f'Вес - {x[0]}, дата:{x[1]}/{x[2]}/{x[3]}',bg='#fcca72',justify=LEFT).pack(pady=5,padx=10)
        Button(self.root,text='Выход',bg='#fcca72',command=self.exit,justify=LEFT).pack(padx=10)
        self.focus()
    def run(self):
        self.drow_widgest()
        if self.flg_exit == True:
            return True
        self.root.mainloop()

    def focus(self):
        self.root.grab_set()
        self.root.focus_set()
        self.root.wait_window()

    def exit(self):
        self.flg_exit = True
        self.root.destroy()