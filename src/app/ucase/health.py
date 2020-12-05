from flask_restful import Resource, reqparse, fields
from src.app.appctx import Appctx
import datetime


class HealthController(Resource):
    def __init__(self):
        self.data = Appctx().data
        self.response = Appctx().response
    
    def get(self):
        # health controller
        return self.response(401, message="OK")


