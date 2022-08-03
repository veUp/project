import tkinter.ttk
from tkinter import *
import tkinter.messagebox as mb
import account


class Registration:
    def __init__(self, parant, width, height, title, rezizable=(False, False)):
        self.root = Toplevel(parant)
        self.root.title(title)
        self.root.resizable(rezizable[0], rezizable[1])
        self.root.iconbitmap('ico.ico')
        self.root.geometry(f'{width}x{height}+600+200')
        self.root.configure(bg='#f3f76a')

        self.login_user = Entry(self.root)
        self.password_user = Entry(self.root, show='*')
        self.age_user = Entry(self.root)
        self.sex_user = Entry(self.root)
        self.choice = tkinter.ttk.Combobox(self.root)
        self.choice['values'] = ('Мужской', 'Женский')

    def draw_widgest(self):
        color = '#f3f76a'
        Label(self.root, text='Логин', justify=LEFT, bg=color).grid(row=0, column=0, sticky=W, pady=5, padx=5)
        Label(self.root, text='Пароль', justify=LEFT, bg=color).grid(row=1, column=0, sticky=W, pady=5, padx=5)
        Label(self.root, text='Возраст', justify=LEFT, bg=color).grid(row=2, column=0, sticky=W, pady=5, padx=5)
        Label(self.root, text='Пол', justify=LEFT, bg=color).grid(row=3, column=0, sticky=W, pady=5, padx=5)
        self.login_user.grid(row=0, column=1, sticky=W + E)
        self.password_user.grid(row=1, column=1, sticky=W + E)
        self.age_user.grid(row=2, column=1, sticky=W + E)
        self.choice.grid(row=3, column=1)

        Button(self.root, text='Сохранить', justify=LEFT, bg='#fcca72', command=self.sq_reg).grid(row=4, column=0,
                                                                                                  sticky=W + S, pady=10,
                                                                                                  padx=10)
        Button(self.root, text='Выход', justify=RIGHT, bg='#fcca72', command=self.root.destroy).grid(row=4, column=3,
                                                                                                     sticky=W + S,
                                                                                                     pady=10, padx=10)
        self.focus()

    def sq_reg(self):
        login = self.login_user.get()
        password = self.password_user.get()
        sex = self.choice.get()
        age = int(self.age_user.get())
        if len(login) == 0 or len(password) == 0 or len(sex) == 0 or age == 0:
            mb.showwarning('Ошибка', 'Ошибка ввода данных!')
        else:
            if sex == 'Мужской':
                sex = 1
            else:
                sex = 0
            bd = account.Data_user(login, password, age, sex)
            ac = bd.run_reg()
            if ac is True:
                mb.showinfo('Регистрация','Вы успешно зарегистрировались!')
            elif ac == 2:
                mb.showwarning('Ошибка', 'Пользователь с таким именем уже существует')
            elif ac == False:
                mb.showwarning('Ошибка', 'Ошибка ввода')

    def run(self):
        self.draw_widgest()
        self.root.mainloop()

    def focus(self):
        self.root.grab_set()
        self.root.focus_set()
        self.root.wait_window()
