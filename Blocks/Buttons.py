import tkinter as tk
import datetime
import time
import sys
import os
import sqlite3 as lite
import Face
sys.path.append(os.path.join(sys.path[0], '../../../Documents/Projects/LaserScan/db/'))
import queryToDataBase



def stay (win):
    win.focus_set() # принять фокус ввода,
    win.grab_set()  # запретить доступ к др. окнам, пока открыт диалог
    win.wait_window() # ждать, пока win не будет уничтожен
def Settings(i):
    win=tk.Toplevel()
    #параметры окна
    win.title("Настройки")
    win.configure(bg='#313440')
    win.resizable(False, False)
    win.geometry('800x600+180+110')

    #области воода IP
    ip1=tk.Entry(win, width=15, font=15)
    iplable1=tk.Label(win, text="IP датчика 1 ",bg='#313440',fg='white').grid(row=0, column=0)

    ip2=tk.Entry(win, width=15, font=15)
    iplable2=tk.Label(win, text="IP датчика 2",bg='#313440',fg='white').grid(row=1, column=0)

    ip3=tk.Entry(win, width=15, font=15)
    iplable3=tk.Label(win, text="IP датчика 3",bg='#313440',fg='white').grid(row=2, column=0)

    bt=tk.Button(win)
    bt.grid(row=3,column=2)

    ip1.grid(row=0, column=1)
    ip2.grid(row=1, column=1)
    ip3.grid(row=2, column=1)

    win.focus_set() # принять фокус ввода,
    win.grab_set()  # запретить доступ к др. окнам, пока открыт диалог
    win.wait_window() # ждать, пока win не будет уничтожен
class New_Change:
    def __init__(self, main):

        self.win=tk.Toplevel()
        #параметры окна
        self.win.title("Настройки")
        self.win.configure(bg='#313440')
        self.win.resizable(False, False)
        self.win.geometry('800x600+180+110')

        self.OperatorName=tk.Entry(self.win, width=15, font=15)
        self.OperatorName.grid(row=0, column=1)
        self.iplable1=tk.Label(self.win, text="Введите имя оператора",bg='#313440',fg='white').grid(row=0, column=0)

        self.BeginDate=tk.Entry(self.win, width=15, font=15)
        self.BeginDate.grid(row=1, column=1)
        self.iplable2=tk.Label(self.win, text="Дата/Время начала смены",bg='#313440',fg='white').grid(row=1, column=0)

        self.EndDate=tk.Entry(self.win, width=15, font=15)
        self.EndDate.grid(row=2, column=1)
        self.iplable3=tk.Label(self.win, text="Дата/Время окончания смены",bg='#313440',fg='white').grid(row=2, column=0)

        self.bt=tk.Button(self.win,text="применить")
        self.bt.place(x=670, y=550,width=120, height=30)


        self.bt.bind("<Button-1>", self.dop)

        self.win.wait_visibility() # window needs to be visible for the grab
        self.win.focus_set() # принять фокус ввода,
        self.win.grab_set()  # запретить доступ к др. окнам, пока открыт диалог
        self.win.wait_window() # ждать, пока win не будет уничтожен

    def dop(self,event):
        txt1=self.OperatorName.get()
        txt2=self.BeginDate.get()
        txt3=self.EndDate.get()
        queryToDataBase.writeToDbChangeTime(txt1,txt2,txt3)
        self.win.destroy()


class SetLog:
    def __init__(self, main):

        self.win=tk.Toplevel()
        #параметры окна
        self.win.title("Партия")
        self.win.configure(bg='#313440')
        self.win.resizable(False, False)
        self.win.geometry('800x600+180+110')

        self.NameSeller=tk.Entry(self.win, width=15, font=15)
        self.NameSeller.grid(row=0, column=1)
        self.lable1=tk.Label(self.win, text="Имя продавца",bg='#313440',fg='white').grid(row=0, column=0)

        self.Bill=tk.Entry(self.win, width=15, font=15)
        self.Bill.grid(row=1, column=1)
        self.lable2=tk.Label(self.win, text="Накладная",bg='#313440',fg='white').grid(row=1, column=0)

        self.transport=tk.Entry(self.win, width=15, font=15)
        self.transport.grid(row=2, column=1)
        self.lable3=tk.Label(self.win, text="Транспорт",bg='#313440',fg='white').grid(row=2, column=0)

        self.Date=tk.Entry(self.win, width=15, font=15)
        self.Date.grid(row=3, column=1)
        self.lable3=tk.Label(self.win, text="Дата/время прибытия",bg='#313440',fg='white').grid(row=3, column=0)


        self.bt=tk.Button(self.win,text="применить")
        self.bt.place(x=670, y=550,width=120, height=30)


        self.bt.bind("<Button-1>", self.dop)

        self.win.wait_visibility() # window needs to be visible for the grab
        self.win.focus_set() # принять фокус ввода,
        self.win.grab_set()  # запретить доступ к др. окнам, пока открыт диалог
        self.win.wait_window() # ждать, пока win не будет уничтожен

    def dop(self,event):
        txt1=self.NameSeller.get()
        txt2=self.Bill.get()
        txt3=self.transport.get()
        txt4=self.Date.get()
        queryToDataBase.writeToDbSetLog(txt1,txt2,txt3,txt4)
        self.win.destroy()








def End_Change(self,event):
    pass
def Start(self,event):
    potok.coordinatStream()
def Stop(self,event):
            pass
def Reports(self,event):
            pass
