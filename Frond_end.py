import tkinter as tk
import  math
import numpy
import socket
import struct
import time
#bg='#313440'
root=tk.Tk()
width=900
height=700
root.title("Lazario  alfa 0.1.0") #Название окна
root.geometry('900x700') #Разрешение окна
root.resizable(False, False) #запрет маштабирования п
BG_Block=   tk.Frame(root, bg='#313440').place(x=0, y = 0 ,width=900, height=700)#Верхнее меню

def alle():
    btn1 = tk.Button(root,text="Начать смену").place(x = 5, y = 5,width=120,height=60)
    btn2 = tk.Button(root,text="Закончить смену").place(x = 130, y =5 ,width=120, height = 60)
    btn3 = tk.Button(root,text="Партия").place(x = 260, y = 5,width=90,height = 60)
    btn4 = tk.Button(root,text="Настройки").place(x = 360, y = 5,width=90,height = 60)
    btn5 = tk.Button(root,text="Старт").place(x = 460, y = 5,width=90,height = 60)
    btn6 = tk.Button(root,text="Стоп").place(x = 560, y = 5,width=90,height = 60)
    btn7 = tk.Button(root,text="Отчёты").place(x = 660, y = 5,width=90,height = 60)

    TopMenu_Block=   tk.Frame(root, bg='#262831').place(x=0, y = 0 ,relwidth=400, height=70)#Верхнее меню
    СhangeTime_Block=tk.Frame(root, bg='#262831').place(x=15, y = 85 ,width=400, height=90)#Время смены
    SetLog_Block=    tk.Frame(root, bg='#262831').place(x=465, y = 85 ,width=400, height=90)#Партия брёвна
    CurrentLog_Block=tk.Frame(root, bg='#262831').place(x=15, y = 190 ,width=850, height=90)#Текущее бревно
    TotalLog_Block=  tk.Frame(root, bg='#262831').place(x=15, y = 295 ,width=850, height=200)#Брёвна в карманах
    Tranporter_Block=tk.Frame(root, bg='#262831').place(x=15, y = 510 ,width=850, height=90)#Состояние транспортёра
    Errors_Block=    tk.Frame(root, bg='#262831').place(x=15, y = 615 ,width=400, height=70)#Ошибки
    DateTime_Block=  tk.Frame(root, bg='#262831').place(x=465, y = 615 ,width=400, height=70)#Время и дата

#btn6 = tk.Button(root,text="Стоп").
alle()
root.mainloop()
