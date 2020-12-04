from flask_restful import Resource, reqparse, fields
from src.app.helpers.rest import response
import datetime
# from src.models import model as db


class HealthController(Resource):
    def get(self):
        return response(200, message="OK")


