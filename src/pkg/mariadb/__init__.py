import pymysql
from pymysql import cursors

class MySQL(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        if hasattr(app, 'teardown_appcontext'):
            app.teardown_appcontext(self.teardown)

    @property
    def connect(self):
        if self.app.config['pymysql_kwargs']:
            kwargs = self.app.config['pymysql_kwargs']
            if 'cursorclass' in kwargs.keys():
                kwargs['cursorclass'] = getattr(cursors, kwargs['cursorclass'])
        else:
            kwargs = dict()

        return pymysql.connect(**kwargs)

    @property
    def connection(self):
        try:
            ctx = self.app.app_context()
            if ctx is not None:
                if not hasattr(ctx, 'mysql_db'):
                    ctx.mysql_db = self.connect
                return ctx.mysql_db
        except Exception as e:
            print("Eror: ", e)

    def teardown(self, exception):
        ctx = self.app.app_context()
        if hasattr(ctx, 'mysql_db'):
            ctx.mysql_db.close()