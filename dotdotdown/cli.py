#!/usr/bin/env python
# coding: utf-8
from __future__ import unicode_literals

import os
import sys
import logging

base_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.insert(0, base_path)

from dotdotdown.lib.parse.cmdline import cmd_line
from dotdotdown.lib.core.data import conf, paths, logger
from dotdotdown.lib.core.downloader import DownLoader


def set_log_level(log_level):
    """

    :param log_level:
    :return:
    """
    if 'debug' in log_level:
        logger.setLevel(logging.DEBUG)
    elif 'warning' in log_level:
        logger.setLevel(logging.WARNING)
    elif 'error' in log_level:
        logger.setLevel(logging.ERROR)
    else:
        logger.setLevel(logging.INFO)


def main():
    """

    :return:
    """
    try:
        cmd_line()

        paths.ROOT_PATH = base_path

        set_log_level(conf.log_level)

        down = DownLoader(
            url=conf.url,
            output_dir=conf.output_dir,
            dir_depth=conf.dir_depth,
            timeout=conf.timeout,
            max_try_count=conf.max_try_count,
        )
        down.start()

    except KeyboardInterrupt:
        logger.error("User aborted.")

    except EOFError:
        logger.error("exit")

    except SystemExit:
        pass


if __name__ == '__main__':
    main()




