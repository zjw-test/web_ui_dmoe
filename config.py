import logging
import logging.handlers
import os
from datetime import datetime

FILE_LOCATION = os.path.dirname(__file__)


def config_log():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    cmd = logging.StreamHandler()
    today = datetime.now().strftime('%Y-%m-%d')
    file = logging.handlers.TimedRotatingFileHandler(
        FILE_LOCATION + os.sep + "log" + os.sep + 'demo_log_{0}.log'.format(today),
        when='midnight', interval=1, backupCount=3,
        encoding='utf-8')
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt=fmt)
    file.setFormatter(formatter)
    cmd.setFormatter(formatter)
    logger.addHandler(cmd)
    logger.addHandler(file)
