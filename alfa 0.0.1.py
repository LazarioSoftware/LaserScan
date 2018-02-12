import tkinter as tk
import  math
import numpy
import socket
import struct
import time

def take_ip():
    ip=gate.get()
    print(ip)
    return(ip)
def send_it(ip,i): #функция отправления команд
    host = str(ip) #хост датчика
    print(host)
    p=11681 #порт датчика
    adres =('192.168.1.150',55555)
    print(i)
    #i=struct.pack('Bb',com,arg)#паковка  команды
    sock=socket.socket(socket.AF_INET,
                   socket.SOCK_DGRAM)
    sock.bind(adres)
    sock.sendto(i, (host, p)) #отсылка команды)
    print('отправил')
    i1, addr = sock.recvfrom(4104)
    #l=sock.getsockname()#получение ip и порта откуда был сделан запрос в вормате tupel
    #print("port, ip destination",l)
    return (i1)


def message(cmd):
    Message_win=tk.Message(root, text=cmd, width=300,bg='#FFFFFF').place(x=100, y = 0 ,width=300, height =240)
def lazer_on():
    i=b'\x81\x20\x01\x01'
    message("it working")
    send_it(take_ip(),i)
def lazer_off():
    i=b'\x81\x20\x01\x00'
    message("lazer off")
    send_it(take_ip(),i)
def settings():
    message("settings")
    print("settings")
def run():
        i=b'\x23\x01'
        message(send_it(take_ip(),i))
def stop():
    i=b'\x23\x01'
    message("stoped")
    send_it(take_ip(),i)
def graph():
    message("points")
def fist_control_buttoms():
    btn1 = tk.Button(button_win1,text="off",command=lazer_off).place(x = 0, y = 0,width=100,height = h)
    btn2 = tk.Button(button_win1,text="on",command=lazer_on).place(x = 0, y = h,width=100, height = h)
    btn3 = tk.Button(button_win1,text="settings",command=settings).place(x = 0, y = h*2,width=100,height = h)
    btn4 = tk.Button(button_win1,text="run",command=run).place(x = 0, y = h*3,width=100, height = h)
    btn5 = tk.Button(button_win1,text="stop",command=stop).place(x = 0, y = h*4,width=100, height = h)
    btn6 = tk.Button(button_win1,text="graph",command=graph).place(x = 0, y = h*5,width=100, height = h)

root=tk.Tk()
width=400
height=240
root.title("Alfa 0.0.1") #Название окна
root.geometry('400x280') #Разрешение окна
message(" ")

button_win1=tk.Frame(root).place(x=0, y = 0 ,width=100, height =240)
h=height/6 #нужно для расположения кнопок у окне
fist_control_buttoms()

gate=tk.Entry(root,bd=5)
gate.insert(0, '')
gate.place(x=100, y = 240 ,width=140, height =40)



root.mainloop()
