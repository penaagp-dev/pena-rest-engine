import logging
from pythonjsonlogger import jsonlogger
from datetime import datetime

class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        if not log_record.get('time'):
            now = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
            log_record['time'] = now
        
        if log_record.get('level'):
            log_record['level'] = log_record['level'].lower()
        else:
            log_record['level'] = record.levelname
        
        log_record["function"] = __name__
        log_record["line"] = str(record.lineno)

def setup_log():
    formatter = CustomJsonFormatter('%(time)s %(level)s %(function)s %(message)s %(line)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger = logging.getLogger(__name__)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False
    return logger

def info(msg, event=None):
    logger = setup_log()
    event = {
        "event": event
    }
    logger.info(msg, extra=event)

def error(msg, event=None):
    logger = setup_log()
    event = {
        "event": event
    }
    logger.error(msg, extra=event)

def warning(msg, event=None):
    logger = setup_log()
    event = {
        "event": event
    }
    logger.warning(msg, extra=event)