from src.pkg.mariadb import get_connection
from src.app import app

conn = get_connection(app)
print("Connection:> ",conn)
# cusor = conn.cursor()