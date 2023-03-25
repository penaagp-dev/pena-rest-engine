from src.app.repository import mysql

def insert():
   return mysql.fetch("SELECT * FROM tb_board LIMIT 1", None)

