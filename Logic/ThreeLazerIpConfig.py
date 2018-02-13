import numpy as np
import time
import socket
import struct
from math import *
import sys
import os
sys.path.append(os.path.join(sys.path[0], '../'))
import Face



def prin(i):
    print("7")
    if (i==1):
        Face.IPcontrol.ok(root)
    elif (i==0):
        Face.IPcontrol.neok(root)


def connection(ip): #функция отправления команд
    host = str(ip) #хост датчика
    p=11681 #порт датчика
    print(host)
    adres =('192.168.1.150',55555)
    print("1")
    i=b'\xf4'
    #i=struct.pack('Bb',com,arg)#паковка  команды
    sock=socket.socket(socket.AF_INET,
                   socket.SOCK_DGRAM)
    print("2")
    sock.bind(adres)
    print("3")
    sock.sendto(i, (host, p)) #отсылка команды)
    print("4")
    i1, addr = sock.recvfrom(4104)
    k=0
    if (addr==True):
        k=1
    elif (addr==False):
        k=0
    print("5")
    return(k)

    #l=sock.getsockname()#получение ip и порта откуда был сделан запрос в вормате tupel
    #print("port, ip destination",l)
    #return (i1)
