import tkinter as tk
import datetime
import time
import sys
import os

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

    stay(win)

def New_Change(i):
    win=tk.Toplevel()
    #параметры окна
    win.title("Настройки")
    win.configure(bg='#313440')
    win.resizable(False, False)
    win.geometry('800x600+180+110')

    ip1=tk.Entry(win, width=15, font=15)
    iplable1=tk.Label(win, text="Введите имя оператора",bg='#313440',fg='white').grid(row=0, column=0)

    ip2=tk.Entry(win, width=15, font=15)
    iplable2=tk.Label(win, text="Дата/Время начала смены",bg='#313440',fg='white').grid(row=1, column=0)

    ip3=tk.Entry(win, width=15, font=15)
    iplable3=tk.Label(win, text="Дата/Время окончания смены",bg='#313440',fg='white').grid(row=2, column=0)

    bt=tk.Button(win)
    bt.grid(row=3,column=2)

    stay(win)



def End_Change(self,event):
    pass
def Set(self,event):
    pass
def Start(self,event):
    potok.coordinatStream()
def Stop(self,event):
            pass
def Reports(self,event):
            pass
