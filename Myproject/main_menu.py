from tkinter import *
from tkinter import messagebox as mb
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
        self.root.destroy()
        self.flg_exit=True

    def add_mass(self):
        mb.showinfo('lol','azaza')

    def show_history(self):
        pass

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