from flask_mysqldb import MySQL
import os

def get_connection(app):
    app.config["MYSQL_HOST"] = os.environ.get("DB_HOST", "localhost")
    app.config["MYSQL_PORT"] = os.environ.get("DB_PORT", 3306)
    app.config["MYSQL_USER"] = os.environ.get("DB_USER", "root")
    app.config["MYSQL_PASSWORD"] = os.environ.get("DB_PASSWORD", "")
    app.config["MYSQL_DB"] = os.environ.get("DB_NAME", "database")
    
    mariadb = MySQL(app)
    # mariadb.init_app(app)
    return mariadb.connection