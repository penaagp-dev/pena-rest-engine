from yoyo import read_migrations
from .driver import list_driver, config_driver

def rollback_migration(driver="pymysql", path=None):
    config = config_driver[driver]
    backend = list_driver[driver](config)
    sorted_migrations = None
    try:
        migrations = read_migrations(path)
        sorted_migrations = sorted(migrations, key=lambda x: x.id, reverse=True)
    except Exception as e:
        raise e
    else:
        backend.rollback_migrations(sorted_migrations)
        return sorted_migrations
