from src.pkg.mariadb import MySQL
import os

def mysql(app=None):
    app.config['pymysql_kwargs'] = {
        'user': os.environ.get("DB_USER", "localhost"),
        'password': os.environ.get("DB_PASSWORD", "localhost"),
        'host': os.environ.get("DB_HOST", "localhost"),
        'cursorclass': 'DictCursor'
    }
    return MySQL(app)