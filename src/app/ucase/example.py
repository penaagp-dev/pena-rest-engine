from flask_restful import Resource, reqparse, fields
from src.app.appctx import Appctx
from src.app.repository import example
import datetime

class Example(Resource):
    def __init__(self):
        self.data = Appctx().data
        self.response = Appctx().response

    def get(self):
        return self.response(200, message="OK")