from .base import Base
from src.pkg.yoyo import migration
import os, traceback

class Migrate(Base): 
    """
usage:
    migrate up [-p PATH] [-d DRIVER]
    migrate down

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
        if default_path == None:
            default_path = APP_ROOT+"/database/migration"
        if self.args["up"]:
            try:
                migration.run_migration("pymysql", default_path)
            except Exception as e:
                print(e)
            else:
                print("Migration Successfully")
                exit(0)
        if self.args["down"]:
            print("Coming Soon")
            exit(0)
