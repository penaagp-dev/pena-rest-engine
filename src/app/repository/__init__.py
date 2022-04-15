from src.app import package

mysql = package.mysql()
conn = mysql.connection

print(package.boto().clients)