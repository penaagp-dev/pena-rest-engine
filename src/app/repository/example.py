from src.app.repository import mysql

cur = mysql.cursor()
def insert():
    try:
        cur.execute("SELECT * FROM guest")
    except Exception as e:
        raise e
    else:
        return cur.fetchall()

