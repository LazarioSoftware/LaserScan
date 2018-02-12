from tkinter import *
import datetime
class qestion:
    def __init__(self, main):
        self.e1=Entry(main, width=3,font=15)
        self.bt1=Button(main,text="Check")
        self.la1=Label(main,width=27, font=15)

        self.e1.grid(row=0, column=0)
        self.bt1.grid(row=0, column=1)
        self.la1.grid(row=0, column=2)

        self.bt1.bind("<Button-1>", self.answer)

    def answer(self, event):
        txt=self.e1.get()
        try:
            if int(txt)<18:
                self.la1["text"]=datetime.datetime.now()
            else:
                self.la1["text"]="да"
        except ValueError:
            self.la1["text"]="херня"


root=Tk()
q=qestion(root)
root.mainloop()
