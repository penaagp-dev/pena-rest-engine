from flask_restful import Resource, reqparse, fields
from src.app.helpers.rest import response
from src.app.repository import example
import datetime

class Example(Resource):
    def get(self):
        example.insert("OK")
        return response(200, message="OK")