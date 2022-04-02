from src.pkg.mariadb import get_cursor
from src.app import app

__conn___ = get_connection()
__cursor__ = __conn___.cursor()