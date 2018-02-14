import numpy as np
import time
import socket
import struct
from math import *
import matplotlib.pyplot as plt

def get_slice():
    i = 8
    step = 4
    ln = len(bv)
    while i < ln:
        yield bv[i:i+step]
        i += step

def int16_to_float_pryamoy(i):
     bit = 7  # Колличество дробных битов

     a = i >> bit        # целая часть
     b = i & (2**bit-1)  # дробная часть
     return float('%d.%d' % (a, b))
def int16_to_float_dop(i):
     bit = 7  # Колличество дробных битов
     a = i >> bit        # целая часть
     b = i & (2**bit-1)  # дробная часть
     return float('%d.%d' % (a, b))



def search_port(com): #функция определения порта с которого был отправлен запрос
    host = '192.168.1.133' #хост датчика
    p=11681 #порт датчика

    adres =('192.168.1.150',55555)

    i=struct.pack('B',com)#паковка  команды
    print('упоковал',i)
    #i=b'x20\x00\x00\x00\x00\x00\x00\x00'
    #i2=b'x01'

    sock=socket.socket(socket.AF_INET,
                   socket.SOCK_DGRAM)
    sock.bind(adres)
    sock.sendto(i, (host, p)) #отсылка команды)
    print('отправил')
    i1, addr = sock.recvfrom(4104)
    l=sock.getsockname()#получение ip и порта откуда был сделан запрос в вормате tupel
    print("port, ip destination",l)
    return (i1)





while True:
    com=int((input("Command->")))

    bv=search_port(com)
    print('ответ:',bv)
    print(struct.unpack('hh', bv))
'''
    for i in get_slice():
            h,w=struct.unpack('hh', i)

            #print(int16_to_float_pryamoy(h),int16_to_float_dop(w))
'''


'''
#print(bv)
print('______')
z=8
while z<len(bv):
    print(bv[z],bin(bv[z]))

    z=z+1

tk=b'\xff\xff\xff\xff'

print(struct.unpack
('hh', tk))
'''

        #struct.iter_unpack(h,w)
        #print(struct.iter_unpack(h,w))
