from .backend import *
import os

list_driver = {
    "pymysql": mysql
}

config_driver = {
    "pymysql": {
        "host": os.environ.get("DB_HOST", "localhost"),
        "port": os.environ.get("DB_PORT", 3306),
        "name": os.environ.get("DB_NAME", "database"),
        "user": os.environ.get("DB_USER", "root"),
        "password": os.environ.get("DB_PASSWORD", "")
    }
}