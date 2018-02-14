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
        print ("Error %s:")
        sys.exit(1)
    finally:
        if conn:
            conn.close()



#функция записи партии в базу данных
def writeToDbSetLog(seller,sellerpaper,transport,begindatetime):
    try:
        conn = lite.connect('data_writing.db')
        cursor = conn.cursor()
        cursor.executescript("INSERT INTO set_log (seller,seller_paper,transport,begin_datetime) VALUES ('%s','%s','%s','%s')"%(seller,sellerpaper,transport,begindatetime))
        conn.commit()
    except lite.Error:
        if conn:
            conn.rollback()
        print ("Error %s:")
        sys.exit(1)
    finally:
        if conn:
            conn.close()

#цункция записи параметров бревна в базу данных
def writeToDbLogs(codename,poroda,D,L,sbeg,kriv,Dmax,scanningdate):
    try:
        conn = lite.connect('data_writing.db')
        cursor = conn.cursor()
        cursor.executescript("INSERT INTO logs (code_name, poroda, D, L, sbeg, kriv, Dmax, scannig_date) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')"%(codename,poroda,D,L,sbeg,kriv,Dmax,scanningdate))
        conn.commit()
    except lite.Error:
        if conn:
            conn.rollback()
        print ("Error %s:")
        sys.exit(1)
    finally:
        if conn:
            conn.close()
