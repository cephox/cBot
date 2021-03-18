import sys
from logging import getLogger, Logger, Formatter, INFO, StreamHandler


def create_logger() -> Logger:
    logger: Logger = getLogger()
    logger.setLevel(INFO)

    formatter: Formatter = Formatter("[%(asctime)s] [%(levelname)s] %(message)s")

    handler: StreamHandler = StreamHandler(sys.stdout)
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger


logger: Logger = create_logger()
