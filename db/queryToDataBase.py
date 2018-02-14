# -*- coding: utf-8 -*-
import sqlite3 as lite
import sys

#функция записи начала смены в базу данных
def writeToDbChangeTime(operatorname,begindatetime,finishdatetime):
    try:
        conn = lite.connect('data_writing.db')
        cursor = conn.cursor()
        cursor.executescript("INSERT INTO change_time (begin_datetime, finish_datetime, operator_name) VALUES ('%s','%s','%s')"%(begindatetime, finishdatetime, operator_name))
        conn.commit()
    except lite.Error:
        if conn:
            conn.rollback()
        print ("Error")
        sys.exit(1)
    finally:
        if conn:
            conn.close()



#функция записи партии в базу данных
def writeToDbSetLog(seller,sellerpaper,transport,begindatetime):
    try:
        conn = lite.connect('data_writing.db')
        cursor = conn.cursor()
        cursor.executescript("""INSERT INTO set_log (seller,seller_paper,transport,begin_datetime) VALUES ('%s','%s','%s','%s')"""%(seller,sellerpaper,transport,begindatetime))
        conn.commit()
    except lite.Error:
        if conn:
            conn.rollback()
        print ("Error")
        sys.exit(1)
    finally:
        if conn:
            conn.close()

#функция записи параметров бревна в базу данных
def writeToDbLogs(codename,poroda,D,L,sbeg,kriv,Dmax,scanningdate):
    try:
        conn = lite.connect('data_writing.db')
        cursor = conn.cursor()
        cursor.executescript("INSERT INTO logs (code_name, poroda, D, L, sbeg, kriv, Dmax, scannig_date) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')"%(codename,poroda,D,L,sbeg,kriv,Dmax,scanningdate))
        conn.commit()
    except lite.Error:
        if conn:
            conn.rollback()
        print ("Error")
        sys.exit(1)
    finally:
        if conn:
            conn.close()


#функция считывания данных о смене
def readFromDbChangeTime():
    try:
        conn = lite.connect('data_writing.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM change_time WHERE id = (SELECT max(id) FROM change_time)')
        conn.commit()
        unitSetLog = cursor.fetchone()
        return(unitChangeTime)
    except lite.Error:
        if conn:
            conn.rollback()
        print ("Error")
        sys.exit(1)
    finally:
        if conn:
            conn.close()


#функция считывания данных о партии
def readFromDbSetLog():
    try:
        conn = lite.connect('data_writing.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM set_log WHERE id = (SELECT max(id) FROM set_log)')
        conn.commit()
        unitSetLog = cursor.fetchone()
        return(unitSetLog)
    except lite.Error:
        if conn:
            conn.rollback()
        print ("Error")
        sys.exit(1)
    finally:
        if conn:
            conn.close()


#функция считывания данных о бревнах
def readFromDbLogs():
    try:
        conn = lite.connect('data_writing.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM logs WHERE id = (SELECT max(id) FROM logs)')
        conn.commit()
        unitSetLog = cursor.fetchone()
        return(unitLogs)
    except lite.Error:
        if conn:
            conn.rollback()
        print ("Error")
        sys.exit(1)
    finally:
        if conn:
            conn.close()


d=readFromDbSetLog()
print(d[1])
