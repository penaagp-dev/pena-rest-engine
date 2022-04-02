from flask import request

def cast_json():
    return request.get_json(force=True)

def cast_form(params):
    return request.form.get(params)

def cast_params(params):
    return request.args.get(params)