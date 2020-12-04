from .base import Base
from src.app import create_app
import os

class Http(Base): 
    """
usage:
    http serve

Command:

Options:
-h --help                             Print usage
    """

    def execute(self):
        if self.args["serve"]:
            app = create_app()
            app.run(host=os.environ.get('APP_HOST', 'localhost'),
                    port=int(os.environ.get('APP_PORT', 8081)))
            exit(0)
