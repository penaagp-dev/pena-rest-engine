from flask_restful import Resource, reqparse, fields
from src.app.appctx import result
import datetime


class HealthController(Resource):   
    def get(self):
        # health controller
        return result.response(200, message="OK")


