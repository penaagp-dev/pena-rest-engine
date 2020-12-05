import arrow
from src.consts import appctx


def response(status_code, message=None, data=None):
    """Response data helper

    Arguments:
        status_code {int} -- http status code

    Keyword Arguments:
        message {string} -- response message (default: {None})
        data {dict} -- data to be appended to response (default: {None})

    Returns:
        dict -- response data
    """
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
