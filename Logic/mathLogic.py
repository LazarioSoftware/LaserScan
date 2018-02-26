# -*- coding: utf-8 -*-
import sqlite3 as lite
import sys
import numpy

#метод серединного сечения
def metodSredSechV (L,dSred): #на вход в мм принимает длину и срединный диаметр
    Lm = L * (10 ** -3)
    velichina = -2
    dSredSm = dSred * (10 ** velichina)
    Vsred = 3.1416 * (dSredSm ** 2) * (Lm/4) * 10000
    return(Vsred) # на выходе объём в м3

#метод концевых сечений
def metodKoncSechV (L,dVerh,Dnizh): # на вход в мм принимает длин бревна, верхний диаметр и нижний диаметр
    Lm = L * (10 ** -3)
    velichina = -2
    dVerhSm = dVerh * (10 ** velichina)
    DnizhSm = Dnizh * (10 ** velichina)
    Vkonc = 3.1416 * ((dVerhSm ** 2) + (DnizhSm ** 2)) * (Lm/8) * 10000
    return(Vkonc) # на выходе объём в м3

#метод верхнего диаметра и среднего сбега
def metodVerhDiamV (L,dVerh,Dnizh): # на в взод в мм принимает длину бревна, верхний диаметр и нижний диаметр
    Lm = L * (10 ** -3)
    Lm = L * (10 ** -3)
    velichina = -2
    dVerhSm = dVerh * (10 ** velichina)
    DnizhSm = Dnizh * (10 ** velichina)
    s = (DnizhSm - dVerhSm) / Lm # значение сбега бревна
    VverhDiam = 3.1416 * Lm * ((dVerhSm + s * (Lm / 2)) ** 2) / 40000
    return(VverhDiam, s)




L=20099
dVerh = 67899.68
Dnizh = 97499.35
dSred=12499.789

print("V концевых сечений = ", metodKoncSechV(L,dVerh,Dnizh), " метров3")
print("V срединного сечения = ", metodSredSechV(L,dSred), "метров3")
print("V верхнего диаметра и среднего сбега = ", metodVerhDiamV(L,dVerh,Dnizh), "метров3")
