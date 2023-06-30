from flask import Blueprint
from flask_restful import Api
from src.app.ucase.health import HealthController
# from src.app.ucase.example import Example

internal_blueprint = Blueprint("internal", __name__, url_prefix='/in')
inAPI = Api(internal_blueprint)
inAPI.add_resource(HealthController, '/health')

# v1 external
external_blueprint = Blueprint("external", __name__, url_prefix='/ex/v1')
# exV1 = Api(external_blueprint)
# exV1.add_resource(Example, '/example')

