"""Logger class.

Log running processes.
"""
# Author: Dongjin Yoon <djyoon0223@gmail.com>

from court_decision_prediction.common.utils import *


class LoggerFactory(metaclass=MetaSingleton):
    """Logger Factory.

    Examples:
        >>> from court_decision_prediction.common.logging import log, dlog
        >>> log("This is printed always")
        >>> dlog("This is printed only when", "--dev")
    """
    filename = f"{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%s')}.log"
    dev      = True

    def __init__(self):
        # Stdout handler
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.DEBUG if self.dev else logging.INFO)

        # File handler
        file_handler = logging.FileHandler(filename=self.filename)
        file_handler.setLevel(logging.DEBUG)

        # Merge handlers
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        logger.addHandler(stream_handler)
        logger.addHandler(file_handler)

        # Exception handling
        sys.excepthook = lambda *args: logger.error("\nUncaught exception:", exc_info=args)
        self.logger = logger

    @classmethod
    def set(cls, yaml_path):
        configs = yaml2dict(yaml_path)
        cls.log_path = join(configs['log_dir'], cls.filename)
        os.makedirs(cls.log_path, exist_ok=True)
        cls.dev = configs['dev']


log  = lambda *msgs: LoggerFactory().logger.info(' '.join(lmap(str, msgs)))
dlog = lambda *msgs: LoggerFactory().logger.debug(' '.join(lmap(str, msgs)))


def initialize_logger(yaml_path):
    LoggerFactory.set(yaml_path)
