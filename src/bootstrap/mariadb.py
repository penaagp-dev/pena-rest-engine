from src.pkg.mariadb import MySQL
import os

def mysql(app=None):
    app.config['pymysql_kwargs'] = {
        'user': os.environ.get("DB_USER", "localhost"),
        'password': os.environ.get("DB_PASSWORD", "localhost"),
        'host': os.environ.get("DB_HOST", "localhost"),
        'db': os.environ.get("DB_NAME"),
        "charset": 'utf8',
        'cursorclass': 'DictCursor'
    }
    return MySQL(app)