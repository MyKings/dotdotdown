#!/usr/bin/python
# coding:utf-8

import time
import os
import argparse

from dotdotdown import __version__
from dotdotdown.lib.core.data import conf


def cmd_line():
    """

    :return:
    """
    print """
    .___      __      .___      __      .___                   
  __| _/_____/  |_  __| _/_____/  |_  __| _/______  _  ______  
 / __ |/  _ \   __\/ __ |/  _ \   __\/ __ |/  _ \ \/ \/ /    \\ 
/ /_/ (  <_> )  | / /_/ (  <_> )  | / /_/ (  <_> )     /   |  \\
\____ |\____/|__| \____ |\____/|__| \____ |\____/ \/\_/|___|  /
     \/                \/                \/                 \/ 

        Author: MyKings Version: %s/%s\n
===========================================================================
""" % (__version__, time.strftime("%Y%m%d", time.gmtime(os.path.getctime(__file__))))
    parser = argparse.ArgumentParser(description='')

    options = parser.add_argument_group('Options Group')

    options.add_argument('-u', '--url', dest='url',
                         help='The url address to download.')

    options.add_argument('-o', '--output-dir', dest='output_dir', default='output',
                         help='Output directory.')

    options.add_argument('--file-ext', dest='file_ext', default='*.*',
                         help='Only allowed file extensions, default(*.*)')

    options.add_argument('--dir-depth', dest='dir_depth', type=int, default=0,
                         help='The maximum depth of the directory, the default is 0 is not limited')

    options.add_argument('-l', '--log-level', dest='log_level', default='info',
                         choices=['info', 'debug', 'warning', 'error'],
                         help='Set the log level, default:(info)')
    options.add_argument('--timeout', dest='timeout', default=5, type=int,
                         help='HTTP request timeout, default:(5s)')
    options.add_argument('--max-try-count', dest='max_try_count', default=5, type=int,
                         help='Maximum number of attempts to connect after timeout, default:(5)')

    options.add_argument('--proxy-socks', dest='proxy_socks',
                         help='Set requests to use the socks proxy, format:"socks5://127.0.0.1:1080"')

    options.add_argument('--enable-proxychains4', dest='enable_proxychains4', action='store_true',
                         help='Download using proxychains4 proxy, The download method is "proxychains4 wget '
                              'http://exmaple.com/1.txt -O 1.txt"')

    args = parser.parse_args()

    conf.url = args.url
    conf.output_dir = args.output_dir
    conf.dir_depth = args.dir_depth
    conf.timeout = args.timeout
    conf.max_try_count = args.max_try_count
    conf.file_ext = args.file_ext
    conf.proxy_socks = args.proxy_socks
    conf.enable_proxychains4 = args.enable_proxychains4
    conf.log_level = args.log_level

    if not any((conf.url,)):
        parser.print_help()
        exit(0)

