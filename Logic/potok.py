import numpy
import time
import socket
import struct

'''
Переменная mass типа лист содержит в себе координаты,
Xn - растояние
Xn+1 - боковое смещение
'''
def coordinatStream ():
    def get_slice():#слайсер

        i = 8
        step = 4
        ln = len(i1)
        while i < ln:
            yield i1[i:i+step]
            i += step

    while True:
        time.sleep(1)
        host = '192.168.1.132' #хост датчика
        p=11681 #порт датчика

        adres =('192.168.1.150',55555)
        com=34#комманда отправить профиль из защёлки
        i=struct.pack('B',com)#паковка  команды

        sock=socket.socket(socket.AF_INET,
                       socket.SOCK_DGRAM)
        sock.bind(adres)
        sock.sendto(i, (host, p)) #отсылка команды)
        print('отправил')
        i1, addr = sock.recvfrom(4104)
        l=sock.getsockname()#получение ip и порта откуда был сделан запрос в вормате tupel
        print("port, ip destination",l)
        #print(i1)
        print("__________")

        n=1
        mas=[]
        for i in get_slice():
            data = i
            x = numpy.uint16(data[0]*256 + data[1]) / 32
            y = numpy.int16(data[2]*256 + data[3]) / 32

            mas.append(x)#добавляет в конец стиска значение растояние
            mas.append(y)#добавляет в конец списка боковое смещение
            n=n+1

        return(mas)
