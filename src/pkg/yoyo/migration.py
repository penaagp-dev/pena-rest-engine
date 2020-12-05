from yoyo import read_migrations
from .driver import list_driver, config_driver

def run_migration(driver="pymysql", path=None):
    
    config = config_driver[driver]
    backend = list_driver[driver](config)
    try:
        migrations = read_migrations(path)
        backend.apply_migrations(backend.to_apply(migrations))
    except Exception as e:
        raise e
