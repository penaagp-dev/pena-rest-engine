from .base import Base
# from src.pkg.yoyo import migration, rollback
from sys import exit
import os, traceback

class Migrate(Base): 
    """
usage:
    migrate up [-p PATH] [-d DRIVER]
    migrate down [-p PATH] [-d DRIVER]
    migrate create

Command:
    up                                  start migrating
    down                                down migrating
Options:
-h --help                               Print usage
-p path --path=PATH                     Load migration path
-d driver --driver=DRIVER               Choose your driver
    """

    def execute(self):
        APP_ROOT = os.path.join(os.path.dirname(__file__), '../..')
        default_path = self.args["--path"]
        default_driver = self.args["--driver"]
        # setup default value
        # if default_path == None:
        #     default_path = APP_ROOT+"/database/migration"
        # if default_driver == None:
        #     default_driver = "pymysql"

        # if self.args["up"]:
        #     try:
        #         migration.run_migration(default_driver, default_path)
        #     except Exception as e:
        #         print(e)
        #         exit(1)
        #     else:
        #         print("Migration Successfully")
        #         exit(0)
        
        # if self.args["down"]:
        #     try:
        #         rollback.rollback_migration(default_driver, default_path)
        #     except Exception as e:
        #         print(e)
        #         exit(1)
        #     else:
        #         print("Rollback Successfully")
        #         exit(0)

        # if self.args["create"]:
        #     print("Coming Soon")
        #     exit(0)
