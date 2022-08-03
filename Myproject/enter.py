import account
import tkinter.messagebox as mb
from tkinter import *


class Enter:
    def __init__(self, parent):
        self.root = Toplevel(parent)
        self.login_user = Entry(self.root)
        self.password_user = Entry(self.root, show='*')
        self.color = '#f3f76a'
        self.root.title('Авторизация')
        self.root.resizable(False, False)
        self.root.iconbitmap('ico.ico')
        self.root.geometry('250x150+600+300')
        self.root.configure(bg=self.color)

    def draw_widgets(self):
        color = '#f3f76a'
        Label(self.root, text='Логин', justify=LEFT, bg=color).grid(row=0, column=0, sticky=W, pady=5, padx=5)
        Label(self.root, text='Пароль', justify=LEFT, bg=color).grid(row=1, column=0, sticky=W, pady=5, padx=5)
        self.login_user.grid(row=0, column=1, sticky=W + E)
        self.password_user.grid(row=1, column=1, sticky=W + E)

        Button(self.root, text='Вход', justify=LEFT, bg='#fcca72', command=self.ent).grid(row=4, column=0, sticky=W + S,
                                                                                          pady=10, padx=10)
        Button(self.root, text='Выход', justify=RIGHT, bg='#fcca72', command=self.root.destroy).grid(row=4, column=3,
                                                                                                     sticky=W + S,
                                                                                                    pady=10, padx=10)
        self.focus()
    def ent(self):
        login = self.login_user.get()
        password = self.password_user.get()
        start = account.Data_user(login, password, None, None)
        flg = start.user_enter()
        if flg:
            mb.showinfo('Вход.', f'Добро пожаловать, {login}')
            self.root.destroy()
            return login
        elif flg is False:
            mb.showwarning('Ошибка', 'Неверный логин или пароль')

    def run(self):
        self.draw_widgets()
        self.root.mainloop()

    def focus(self):
        self.root.grab_set()
        self.root.focus_set()
        self.root.wait_window()
