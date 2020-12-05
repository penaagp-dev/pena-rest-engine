import arrow
from src.consts import appctx
from flask import request




class Appctx():
    def data(self):
        return request.get_json(force=True)

    def response(self, status_code, message=None, data=None):
        status = {}
        status['data'] = data if data else None
        status['code'] = status_code
        if status_code in appctx.success_status:
            status['status'] = appctx.success_status[status_code]
            status['message'] = message if message else appctx.success_status[status_code]
        elif status_code in appctx.failure_status:
            status['status'] = appctx.failure_status[status_code]
            status['message'] = message if message else appctx.failure_status[status_code]
        else:
            status['status'] = appctx.failure_status[status_code]
            status['message'] = message if message else appctx.failure_status[400]
        return status
        
