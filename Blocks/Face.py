from tkinter import *
import datetime
import time
import sys
import os
sys.path.append(os.path.join(sys.path[0], '../../../Документы/Projects/LaserScan/Logic/'))
import ThreeLazerIpConfig

class TopMenu:
    def __init__(self, main):

        self.btn1=Button(main,text="Начать смену",bg='#262831',fg='#FFFFFF',font='arial 12')
        self.btn1.grid(row=0, column=0)
        self.btn2=Button(main,text="Закончить смену",bg='#262831',fg='#FFFFFF',font='arial 12')
        self.btn2.grid(row=0, column=1)
        self.btn3=Button(main,text="Партия",bg='#262831',fg='#FFFFFF',font='arial 12')
        self.btn3.grid(row=0, column=2)
        self.btn4=Button(main,text="Настройки",bg='#262831',fg='#FFFFFF',font='arial 12')
        self.btn4.grid(row=0, column=3)
        self.btn5=Button(main,text="Старт",bg='#262831',fg='#FFFFFF',font='arial 12')
        self.btn5.grid(row=0, column=4)
        self.btn6=Button(main,text="Стоп",bg='#262831',fg='#FFFFFF',font='arial 12')
        self.btn6.grid(row=0, column=5)
        self.btn7=Button(main,text="Отчёты",bg='#262831',fg='#FFFFFF',font='arial 12')
        self.btn7.grid(row=0, column=6)

        self.btn1.bind("<Button-1>", self.New_Change)
        self.btn2.bind("<Button-1>", self.End_Change)
        self.btn3.bind("<Button-1>", self.Set)
        self.btn4.bind("<Button-1>", self.Settings)
        self.btn5.bind("<Button-1>", self.Start)
        self.btn6.bind("<Button-1>", self.Stop)
        self.btn7.bind("<Button-1>", self.Reports)

    def Settings(self,event):
            self.win=Toplevel()
            #параметры окна
            self.win.title("Настройки")
            self.win.configure(bg='#313440')
            self.win.resizable(False, False)
            self.win.geometry('800x600+180+110')

            #области воода IP
            self.ip1=Entry(self.win, width=15, font=15)
            self.iplable1=Label(self.win, text="IP датчика 1 ",bg='#313440',fg='white').grid(row=0, column=0)

            self.ip2=Entry(self.win, width=15, font=15)
            self.iplable2=Label(self.win, text="IP датчика 2",bg='#313440',fg='white').grid(row=1, column=0)

            self.ip3=Entry(self.win, width=15, font=15)
            self.iplable3=Label(self.win, text="IP датчика 3",bg='#313440',fg='white').grid(row=2, column=0)
            def con_fig():
                txt1=self.ip1.get()
                if (ThreeLazerIpConfig.connection(txt1)==1):
                    ThreeLazerIpConfig.prin(1)
                    print("6")
                elif (ThreeLazerIpConfig.connection(txt1)==0):
                    print("6")
                    ThreeLazerIpConfig.prin(0)



            self.bt=Button(self.win,command=con_fig)
            self.bt.grid(row=3,column=2)

            self.ip1.grid(row=0, column=1)
            self.ip2.grid(row=1, column=1)
            self.ip3.grid(row=2, column=1)


            self.win.focus_set() # принять фокус ввода,
            self.win.grab_set()  # запретить доступ к др. окнам, пока открыт диалог
            self.win.wait_window() # ждать, пока win не будет уничтожен
    def New_Change(self,event):
            self.win=Toplevel()


            self.win.title("Начало смены")
            self.win.configure(bg='#313440')
            self.win.resizable(False, False)
            self.win.geometry('800x600+100+200')

            self.ip1=Entry(self.win, width=15, font=15)
            self.iplable1=Label(self.win, text="Имя оператора ",bg='#313440',fg='white').grid(row=0, column=0)

            self.ip2=Entry(self.win, width=15, font=15)
            self.iplable2=Label(self.win, text="IP датчика 2",bg='#313440',fg='white').grid(row=1, column=0)

            self.ip3=Entry(self.win, width=15, font=15)
            self.iplable3=Label(self.win, text="IP датчика 3",bg='#313440',fg='white').grid(row=2, column=0)

            self.bt.grid(row=3,column=2)

            self.ip1.grid(row=0, column=1)
            self.ip2.grid(row=1, column=1)
            self.ip3.grid(row=2, column=1)

            self.win.focus_set() # принять фокус ввода,
            self.win.grab_set()  # запретить доступ к др. окнам, пока открыт диалог
            self.win.wait_window() # ждать, пока win не будет уничтожен
    def End_Change(self,event):
            pass
    def Set(self,event):
            pass
    def Start(self,event):
            pass
    def Stop(self,event):
            pass
    def Reports(self,event):
            pass
class ChangeTime:
    def __init__(self, main):
        self.frame=Frame(main,bg='#262831',).place(x=15, y=55,width=400, height=90)
        l0=Label(self.frame,text="Начало смены",bg='#262831',fg='white').place(x=15, y=55)

        l1=Label(self.frame,text="Номер смены:",bg='#262831',fg='white',font=5).place(x=15, y=75)
        l2=Label(self.frame,text="Дата/время:",bg='#262831',fg='white',font=5).place(x=15, y=95)
        l2=Label(self.frame,text="Фамилия:",bg='#262831',fg='white',font=5).place(x=15, y=115)

        #l11=Label(self.frame,text="...:",bg='#262831',fg='white',font=5).place(x=15, y=75)
        #l21=Label(self.frame,text="....",bg='#262831',fg='white',font=5).place(x=15, y=95)
        #l21=Label(self.frame,text="Фамилие:",bg='#262831',fg='white',font=5).place(x=15, y=115)
class SetLog:
    def __init__(self, main):
        self.SetLog_Block=Label(main, text="SetLog_Block",bg='#262831',fg='white').place(x=465, y=85,width=400, height=90)#Верхнее меню
class CurrentLog:
    def __init__(self, main):
        self.СurrentLog_Block=Label(main, bg='#262831',fg='white').place(x=15, y = 190 ,width=850, height=90)
        IndicatorBox_list=["Имя Бревна","Пoрода","D,mm","L,mm","Сбег","Кривизна %","V,m"]
        n=0
        for i in IndicatorBox_list:
            #rel=""
            #cmd=lambda x=i:
            self.la1=Label(main, text=i)
            self.la1.place(x=15+n, y =190)
            n=n+137
class TotalLog:
    pass
class Trancporter:
    pass
class Errors:
    pass
class DateTime:
    def __init__(self, main):
        self.clock_frame=Label(main,height=7,width=7,bg='#262831',fg='white',font=10)
        self.clock_frame.place(x=465, y = 590 ,width=400, height=70)#Время и дата
        def tick (time1=''):
            now=time.strftime(' %H:%M:%S ')
            date=time.strftime(' %d.%m.%Y ')
            if (now!=time1):
                b=('Дата:'+date)
                b1=('Время:'+now)
                global c
                c=b+b1
                time1=now
                self.clock_frame.configure(text=c)
            self.clock_frame.after(200, tick)
        tick()
class IPcontrol:
    def __init__(self, main):
        self.ipTEXT1=Label(main, text="IP 1 ",bg='#313440',fg='white').place(x=1, y=670)
        self.ipTEXT2=Label(main, text="IP 2",bg='#313440',fg='white').place(x=380, y=675)
        self.ipTEXT3=Label(main, text="IP 3",bg='#313440',fg='white').place(x=750, y=670)
    def ok(self, main):
        self.ipVALUE1=Label(main, text="connected",bg='#313440',fg='green').place(x=30, y=670)
        self.ipVALUE2=Label(main, text=" connected",bg='#313440',fg='green').place(x=410, y=675)
        self.ipVALUE3=Label(main, text=" connected",bg='#313440',fg='green').place(x=780, y=670)
    def neok(self, main):
        self.ipVALUE1=Label(main, text="Error",bg='#313440',fg='red').place(x=30, y=670)
        self.ipVALUE2=Label(main, text="Error",bg='#313440',fg='red').place(x=410, y=675)
        self.ipVALUE3=Label(main, text="Error",bg='#313440',fg='red').place(x=780,y=670)
