import os
from src.pkg.mariadb import MySQL
from src.pkg.boto import Boto3

class Bootstrap(object):
    def __init__(self, app=None):
        self.app = app

    def mysql(self):
        self.app.config['pymysql_kwargs'] = {
            'user': os.environ.get("DB_USER", "localhost"),
            'password': os.environ.get("DB_PASSWORD", "localhost"),
            'host': os.environ.get("DB_HOST", "localhost"),
            'db': os.environ.get("DB_NAME"),
            'port': int(os.environ.get("DB_PORT")),
            "charset": 'utf8',
            'cursorclass': 'DictCursor'
        }
        return MySQL(self.app).connect

    def boto(self):
        self.app.config["BOTO3_REGION"] = os.environ.get("AWS_REGION", "ap-southeast-1")
        self.app.config["BOTO3_ACCESS_KEY"] = os.environ.get("AWS_ACCESS_KEY", "")
        self.app.config["BOTO3_SECRET_KEY"] = os.environ.get("AWS_SECRET_KEY", "")
        self.app.config["BOTO3_PROFILE"] = os.environ.get("AWS_PROFILE", "default")
        self.app.config['BOTO3_SERVICES'] = ['s3']
        return Boto3(self.app)


