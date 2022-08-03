from tkinter import *

class Window:
    def __init__(self,parent):
        self.root = Toplevel(parent)
        self.root.geometry('300x300+600+300')
        self.root.iconbitmap('ico.ico')
        self.root.configure(bg='#f3f76a')
        self.add_mass = Entry(self.root)
        self.show_history = Entry(self.root)
        # self.exit = Entry(self.root)
        self.flg_exit = False



    def draw_widgest(self):
        Button(self.root, text='Запись веса', justify=CENTER, bg='#fcca72', command=self.add_mass).grid(row=0, column=1, sticky=W + S,pady=10, padx=10)
        Button(self.root, text='Показать историю', justify=CENTER, bg='#fcca72', command=self.show_history).grid(row=0, column=1, sticky=W + S,pady=10, padx=10)
        Button(self.root, text='Выход в главное меню', justify=CENTER, bg='#fcca72', command=self.exit).grid(row=0, column=1, sticky=W + S,pady=10, padx=10)

        self.focus()
    def exit(self):
        self.root.destroy()
        self.flg_exit=True

    def add_mass(self):
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