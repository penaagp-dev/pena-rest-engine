from dotenv import load_dotenv, find_dotenv
from src.pkg.meta import MetaFlaskEnv
import os

APP_ROOT = os.path.join(os.path.dirname(__file__), '../..')
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

def config():
    try:
        load_dotenv(dotenv_path=dotenv_path, verbose=True)
    except Exception as e:
        print("Error: ", e)
        exit(1)


class Config(metaclass=MetaFlaskEnv):
    ENV_PREFIX = "FLASK_"