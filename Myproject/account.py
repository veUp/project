import sqlite3 as sq
from os import path
import tkinter.messagebox as mb

class Data_user:
    def __init__(self, login, password, age, sex):
        self.login = login
        self.password = password
        self.age = age
        self.sex = sex
        i = path.isfile('data.db')
        if i:
            self.con = sq.connect('data.db')
            self.cur = self.con.cursor()
            self.cur.execute("""CREATE TABLE IF NOT EXISTS users(
            user TEXT,
            password TEXT,
            sex INTEGER,
            age INTEGER
            )
            """)
        else:
            open('data.db', 'w').close()
            self.__init__(login, password, age, sex)

    def user_creat(self):
        login_from = self.cur.execute("""SELECT * FROM users WHERE user=?""",(self.login,))
        one_str = login_from.fetchone()
        try:
            if one_str is None:
                self.cur.execute("""INSERT INTO users VALUES(?,?,?,?)""",(self.login,self.password,self.sex,self.age,))
                self.con.commit()
                self.cur.close()
                return True
            elif one_str is not None:
                return 2
            else:
                return False
        except:
            mb.showwarning('Ошибка','!')
            return False
        finally:
            self.con.commit()

    def user_enter(self):
        enter =self.cur.execute("""SELECT user,password FROM users WHERE user = ? AND password = ?""",(self.login,self.password,))
        if enter.fetchone() is not None:
            return True
        else:
            return False


    def run_reg(self):
        return self.user_creat()

class Mass_user:
    def __init__(self,login=None,mass=None,time=None):
        self.login = login
        if mass is not None and time is not None:
            self.mass = mass
            self.time_year = time[2]
            self.time_mon = time[1]
            self.time_day = time[0]
        i = path.isfile('data.db')
        if i:
            self.con = sq.connect('data.db')
            self.cur = self.con.cursor()
            self.cur.execute("""CREATE TABLE IF NOT EXISTS mass_user(
            user TEXT,
            mass REAL,
            time_year TEXT,
            time_mon TEXT,
            time_day TEXT
            )
            """)
        else:
            open('data.db', 'w').close()
            self.__init__(login, mass, time)

    def add_mass(self):
        try:
            self.cur.execute("""INSERT INTO mass_user VALUES(?,?,?,?,?)""",(self.login,self.mass,self.time_year,
                                                                            self.time_mon,self.time_day,))
            self.con.commit()
            self.con.close()
        except:
            mb.showwarning('Ошибка','Ошибка в блоке сохрания')
        finally:
            self.con.close()

    def show_history(self):
        try:
            # self.cur.execute("""SELECT user FROM mass_user WHERE user = ?""",self.login)
            # data = self.cur.fetchone()
            data_about_mass = self.cur.execute("""SELECT mass,time_year,time_mon,time_day FROM mass_user WHERE user = ?""",(self.login,))
            data = data_about_mass.fetchall()
            self.con.close()
            if len(data)>0:
                return data
            else:
                return False
        except:
            mb.showerror('Ошибка','Ошибка в блоке просмотра')
        finally:
            self.con.close()
