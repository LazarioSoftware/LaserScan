import sqlite3 as lite
import sys

#функция записи начала смены в базу данных
def writeToDbChangeTime(operatorname,begindatetime,finishdatetime):
    try:
        conn = lite.connect('data_writing.db')
        cursor = conn.cursor()
        cursor.executescript("""
            INSERT INTO change_time VALUES (NULL ,'begindatetime', 'finishdatetime', 'operatorname');
            """)
        conn.commit()
    except lite.Error:
        if conn:
            conn.rollback()
        print ("Error %s:")
        sys.exit(1)
    finally:
        if conn:
            conn.close()

operatorname = "Василий"
begindatetime = "07:00 13/02/18"
finishdatetime = "21:00 13/02/18"
writeToDbChangeTime(operatorname,begindatetime,finishdatetime)
