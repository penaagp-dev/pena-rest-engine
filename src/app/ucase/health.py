from flask_restful import Resource, reqparse, fields
from src.app.helpers.rest import response
import datetime


class HealthController(Resource):
    def get(self):
        # health controller
        return response(200, message="OK")


