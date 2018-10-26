# coding:utf-8

import logging
import sys

logger = logging.getLogger(__name__)

try:
    from dotdotdown.lib.core.ansistrm import ColorizingStreamHandler
    logger_handler = ColorizingStreamHandler(sys.stdout)
except ImportError:
    logger_handler = logging.StreamHandler(sys.stdout)

formatter_info = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S")
logger_handler.setFormatter(formatter_info)

logger.addHandler(logger_handler)
logger.setLevel(logging.DEBUG)
