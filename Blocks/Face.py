from tkinter import *
import time
import os
import sys
sys.path.append(os.path.join(sys.path[0], '../../../Документы/Projects/LaserScan/db/'))
import queryToDataBase
import Buttons

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

        self.btn8=Button(main,text="Обновить",bg='#262831',fg='#FFFFFF',font='arial 12')
        self.btn8.grid(row=0, column=7)

        self.btn1.bind("<Button-1>", Buttons.New_Change)
        self.btn2.bind("<Button-1>", Buttons.End_Change)
        self.btn3.bind("<Button-1>", Buttons.SetLog)
        self.btn4.bind("<Button-1>", Buttons.Settings)
        self.btn5.bind("<Button-1>", Buttons.Start)
        self.btn6.bind("<Button-1>", Buttons.Stop)
        self.btn7.bind("<Button-1>", Buttons.Reports)
        self.btn8.bind("<Button-1>", self.update_config)


#Начало смены
        self.frame=Frame(main,bg='#262831',).place(x=15, y=55,width=400, height=130)
        self.ChTimeLabel=Label(self.frame,text="Начало смены",bg='#262831',fg='white').place(x=30, y=55)

        self.ChTime1=Label(self.frame,text="Номер смены:",bg='#262831',fg='white',font=5).place(x=30, y=75)
        self.ChTime2=Label(self.frame,text="Дата/время начала:",bg='#262831',fg='white',font=5).place(x=30, y=95)
        self.ChTime3=Label(self.frame,text="Дата/время окончания:",bg='#262831',fg='white',font=5).place(x=30, y=115)
        self.ChTime4=Label(self.frame,text="Фамилия:",bg='#262831',fg='white',font=5).place(x=30, y=135)

        self.ChTime11=Label(self.frame,text=".....",bg='#262831',fg='white',font=5)
        self.ChTime11.place(x=230, y=75)

        self.ChTime12=Label(self.frame,text=".....",bg='#262831',fg='white',font=5)
        self.ChTime12.place(x=230, y=95)

        self.ChTime13=Label(self.frame,text=".....",bg='#262831',fg='white',font=5)
        self.ChTime13.place(x=230, y=115)

        self.ChTime14=Label(self.frame,text=".....",bg='#262831',fg='white',font=5)
        self.ChTime14.place(x=230, y=135)


#Партия Брёвен
        self.SetLog_Block=Label(main,bg='#262831',fg='white').place(x=450, y=55,width=415, height=130)
        self.SetLogLabel=Label(self.frame,text="Партия",bg='#262831',fg='white').place(x=465, y=55)

        self.SetLog1=Label(self.frame,text="Номер партии:",bg='#262831',fg='white',font=1).place(x=465, y=75)
        self.SetLog2=Label(self.frame,text="Продовец",bg='#262831',fg='white',font=1).place(x=465, y=95)
        self.SetLog3=Label(self.frame,text="Накладная",bg='#262831',fg='white',font=1).place(x=465, y=115)
        self.SetLog4=Label(self.frame,text="Транспорт",bg='#262831',fg='white',font=1).place(x=465, y=135)
        self.SetLog5=Label(self.frame,text="Дата/время прибытия",bg='#262831',fg='white',font=1).place(x=465, y=155)


        self.SetLog11=Label(self.frame,text=".....",bg='#262831',fg='white',font=1)
        self.SetLog11.place(x=695, y=75)

        self.SetLog12=Label(self.frame,text=".....",bg='#262831',fg='white',font=1)
        self.SetLog12.place(x=695, y=95)

        self.SetLog13=Label(self.frame,text=".....",bg='#262831',fg='white',font=1)
        self.SetLog13.place(x=695, y=115)

        self.SetLog14=Label(self.frame,text=".....",bg='#262831',fg='white',font=1)
        self.SetLog14.place(x=695, y=135)

        self.SetLog15=Label(self.frame,text=".....",bg='#262831',fg='white',font=5)
        self.SetLog15.place(x=695, y=155)



        self.СurrentLog_Block=Label(main, bg='#262831',fg='white').place(x=15, y = 200 ,width=850, height=90)
        IndicatorBox_list=["Имя Бревна","Пoрода","D,mm","L,mm","Сбег","Кривизна %","V,m"]
        n=0
        for i in IndicatorBox_list:
            la1=Label(main, text=i)
            la1.place(x=15+n, y =200)
            n=n+137

#Таблица Брёвна
        #self.place=self.Canvas(main, bg='#262831',fg='white').place(x=150, y = 200 ,width=850, height=90)

        '''
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

    def update_config (self, event):
        DbChangeTime=queryToDataBase.readFromDbChangeTime()
        self.ChTime11.configure(text=DbChangeTime[0])#номер смены
        self.ChTime12.configure(text=DbChangeTime[1])#начало
        self.ChTime13.configure(text=DbChangeTime[2])#окончание
        self.ChTime14.configure(text=DbChangeTime[3])#фамилие

        DbSetLog=queryToDataBase.readFromDbSetLog()
        self.SetLog11.configure(text=DbSetLog[0])#номер партии
        self.SetLog12.configure(text=DbSetLog[1])#продавец
        self.SetLog13.configure(text=DbSetLog[2])#Накладная
        self.SetLog14.configure(text=DbSetLog[3])#транспорт
        self.SetLog15.configure(text=DbSetLog[4])#Дата/время
