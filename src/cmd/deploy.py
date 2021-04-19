from .base import Base
from src.app import create_app, app
from sys import exit
import os, traceback

class Deploy(Base): 
    """
usage:
    deploy production  [-n NAME]
    deploy staging  [-n NAME] --debug=<BOOL>
    deploy development  [-n NAME] --debug=<BOOL>

Command:
    deploy                                      start setup deployment

Options:
-h --help                                      Print usage
-n name --name=NAME                            Choose your service name
-d --debug=True                                Debugging | True or False

    """
    def execute(self):
        name = self.args["--name"]
        try:
            debug = self.args["--debug"]
        except Exception:
            debug = "False"
        if self.args["production"]:
            try:
                debug = "False"
                mode = "prd"
                print(name, mode, debug)
            except Exception as e:
                print("Setup error:> ",e)
                exit(1)
            exit(0)
        if self.args["staging"]:
            try:
                
                mode = "stg"
                print(name, mode, debug)
            except Exception as e:
                print("Setup error:> ",e)
                exit(1)
            exit(0)
        if self.args["development"]:
            try:
                debug = self.args["--debug"]
                mode = "dev"
                print(name, mode, debug)

            except Exception as e:
                print("Setup error:> ",e)
                exit(1)
            exit(0)
