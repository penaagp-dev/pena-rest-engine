from src.app import mysql

conn = mysql.connect
curr = conn.cursor()