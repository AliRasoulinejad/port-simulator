import logging


def setup_logger(name):
    formatter = logging.Formatter(fmt='%(module)s - %(funcName)s - %(message)s')

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)

    return logger
