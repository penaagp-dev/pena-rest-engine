import os
from src.config import Config
from flask import Flask
from flask_cors import CORS
# from flask_jwt_extended import JWTManager
# from flask_redis import FlaskRedis

# redis_store = FlaskRedis()
# jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
    
    # redis_store.init_app(app)
    # jwt.init_app(app)

    CORS(app, resources={r"/api/*": {"origins": "*"}})
    from .router import v1_blueprint
    from .router import swaggerui_blueprint

    app.register_blueprint(swaggerui_blueprint, url_prefix=os.environ.get('SWAGGER_URL'))
    app.register_blueprint(v1_blueprint)

    return app
