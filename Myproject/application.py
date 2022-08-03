import tkinter.messagebox
from tkinter import *
import enter
import account
from registration import Registration


class Window:
    def __init__(self, width, height, title='Главное меню', rezizable=(False, False)):
        self.root = Tk()
        self.root.title(title)
        self.root.resizable(rezizable[0], rezizable[1])
        self.root.geometry(f'{width}x{height}+600+200')
        self.root.iconbitmap('ico.ico')
        self.root.configure(bg='#f3f76a')
        self.status = None

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        if self.status is not None:
            Label(self.root,text=self.status,font=16).pack(pady=20)
        Button(self.root, text='Регистрация', width=20, height=2, command=self.reg, bg='#fcca72').pack(pady=20)
        Button(self.root, text='Вход', width=20, height=2, bg='#fcca72', command=self.enter).pack(pady=20)
        Button(self.root, text='Выход', width=20, height=2, command=self.tkquit, bg='#fcca72').pack(pady=20)

    def reg(self, wigth=300, height=180, title='Регистрация', rezizable=(False, False), icon='ico.ico'):
        start = Registration(self.root, wigth, height, title, rezizable)
        start.run()

    def enter(self):
        start = enter.Enter(self.root)
        self.status = start.run()
        print(self.status)

    def tkquit(self):
        ch = tkinter.messagebox.askyesno('Выход', 'Вы хотите выйти?')
        if ch:
            self.root.destroy()


if __name__ == '__main__':
    a = Window(300, 250)
    a.run()