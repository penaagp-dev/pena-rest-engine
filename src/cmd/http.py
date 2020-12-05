from .base import Base
from src.app import create_app, app
from sys import exit
import os, traceback

class Http(Base): 
    """
usage:
    http serve [-e ENV]

Command:
    serve                                      start serve
Options:
-h --help                                      Print usage
-e environment --environment=ENV               Choose your driver

    """

    def execute(self):
        # env_path = self.args["--environment"]
        if self.args["serve"]:
            try:
                httpServe = create_app(app)
                httpServe.run(host=os.environ.get('APP_HOST', 'localhost'),
                    port=int(os.environ.get('APP_PORT', 8081)))
            except Exception as e:
                print(e)
                print(traceback.format_exc())
                exit(1)
            
            exit(0)
