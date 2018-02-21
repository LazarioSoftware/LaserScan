from tkinter import *
import sys
import Buttons
import time
#from TimeFun import tick

class Blocks:
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

        self.btn1.bind("<Button-1>", Buttons.New_Change)
        self.btn2.bind("<Button-1>", Buttons.End_Change)
        self.btn3.bind("<Button-1>", Buttons.Set)
        self.btn4.bind("<Button-1>", Buttons.Settings)
        self.btn5.bind("<Button-1>", Buttons.Start)
        self.btn6.bind("<Button-1>", Buttons.Stop)
        self.btn7.bind("<Button-1>", Buttons.Reports)


        self.frame=Frame(main,bg='#262831',).place(x=15, y=55,width=400, height=90)
        self.l0=Label(self.frame,text="Начало смены",bg='#262831',fg='white').place(x=15, y=55)

        self.l1=Label(self.frame,text="Номер смены:",bg='#262831',fg='white',font=5).place(x=15, y=75)
        self.l2=Label(self.frame,text="Дата/время:",bg='#262831',fg='white',font=5).place(x=15, y=95)
        self.l2=Label(self.frame,text="Фамилия:",bg='#262831',fg='white',font=5).place(x=15, y=115)

                #l11=Label(self.frame,text="...:",bg='#262831',fg='white',font=5).place(x=15, y=75)
                #l21=Label(self.frame,text="....",bg='#262831',fg='white',font=5).place(x=15, y=95)
                #l21=Label(self.frame,text="Фамилие:",bg='#262831',fg='white',font=5).place(x=15, y=115)

        self.SetLog_Block=Label(main, text="SetLog_Block",bg='#262831',fg='white').place(x=465, y=85,width=400, height=90)#Верхнее меню

        #Текущие бревно
        self.СurrentLog_Block=Label(main, bg='#262831',fg='white').place(x=15, y = 190 ,width=850, height=90)
        IndicatorBox_list=["Имя Бревна","Пoрода","D,mm","L,mm","Сбег","Кривизна %","V,m"]
        n=0
        for i in IndicatorBox_list:
            la1=Label(main, text=i)
            la1.place(x=15+n, y =190)
            n=n+137


        '''
        class TotalLog:
            pass
        class Trancporter:
            pass
        class Errors:
            pass
        '''


        #дата и время
        self.clock_frame=Label(main,height=7,width=7,bg='#262831',fg='#FFFFFF',font=15)
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


        self.ipTEXT1=Label(main, text="IP 1 ",bg='#313440',fg='white').place(x=1, y=670)
        self.ipTEXT2=Label(main, text="IP 2",bg='#313440',fg='white').place(x=380, y=675)
        self.ipTEXT3=Label(main, text="IP 3",bg='#313440',fg='white').place(x=750, y=670)

        #self.ipVALUE1=Label(main, text="connected",bg='#313440',fg='green').place(x=30, y=670)
        #self.ipVALUE2=Label(main, text=" connected",bg='#313440',fg='green').place(x=410, y=675)
        #self.ipVALUE3=Label(main, text=" connected",bg='#313440',fg='green').place(x=780, y=670)

        self.ipVALUE1=Label(main, text="Error",bg='#313440',fg='red').place(x=30, y=670)
        self.ipVALUE2=Label(main, text="Error",bg='#313440',fg='red').place(x=410, y=675)
        self.ipVALUE3=Label(main, text="Error",bg='#313440',fg='red').place(x=780,y=670)
