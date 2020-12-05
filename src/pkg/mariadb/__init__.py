import os
import pymysql

def get_connection():
    conn = pymysql.connect(
        host=os.environ.get("DB_HOST"),
        user=os.environ.get("DB_USER"),
        port=int(os.environ.get("DB_PORT")),
        password=os.environ.get("DB_PASSWORD"),
        db=os.environ.get("DB_NAME"),
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor
    )
    return conn

def get_cursor():
    conn = get_connection()
    return conn.cursor()