import os
from src.config import Config
from flask import Flask
from flask_cors import CORS
from src.bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(Config)

bootstrap = Bootstrap(app)

def create_app(app):
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    from .router import internal_blueprint, external_blueprint
    from .router import swaggerui_blueprint
    app.register_blueprint(swaggerui_blueprint, url_prefix=os.environ.get('SWAGGER_URL'))
    app.register_blueprint(internal_blueprint)
    app.register_blueprint(external_blueprint)
    return app
