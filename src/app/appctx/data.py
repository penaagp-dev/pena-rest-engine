from flask import request

def cast():
    return request.get_json(force=True)
