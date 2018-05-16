from conf import setting
import logging.config

def login_auth(func):
    from core import src
    def wrapper(*args,**kwargs):
        if not src.user_dic['username']:
            src.login()
            return func(*args, **kwargs)
        else:
            return func(*args,**kwargs)
    return wrapper

def get_logger(name):
    logging.config.dictConfig(setting.LOGGING_DIC)
    my_logger = logging.getLogger(name)
    return my_logger