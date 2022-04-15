from flask_restful import Resource, reqparse, fields
from src.app.appctx import result
from src.app.repository import example
import datetime

class Example(Resource):
    def get(self):
        data = example.insert()
        return result.response(200, message="OK", data=data)