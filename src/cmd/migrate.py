from .base import Base
import os

class Migrate(Base): 
    """
usage:
    migrate up
    migrate down

Command:
    up                                  start migrating
    down                                down migrating
Options:
-h --help                             Print usage
    """

    def execute(self):
        if self.args["up"]:
            print("Coming Soon")
            exit(0)
        if self.args["down"]:
            print("Coming Soon")
            exit(0)
