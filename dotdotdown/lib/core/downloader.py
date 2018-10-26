# coding: utf-8
from __future__ import unicode_literals

import os
import time
import urlparse
import urllib

import requests
import lxml.html

from dotdotdown import __version__
from dotdotdown.lib.core.data import paths, conf, logger


class Link(object):

    def __init__(self, herf, text, url, parent_url=None, uri_type='dir', save_local_path=None):
        self.herf = herf
        self.text = text
        self.parent_url = parent_url
        self.url = url
        self.uri_type = uri_type
        self.save_local_path = save_local_path


class DownLoader(object):

    def __init__(self, url=None, output_dir=None, file_ext=None, dir_depth=0, timeout=5, max_try_count=5):
        """

        :param url:
        :param output_dir:
        :param file_ext:
        :param dir_depth:
        :param timeout:
        :param max_try_count:
        """
        self.url = url
        self.output_dir = output_dir
        self.file_ext = file_ext
        self.dir_depth = dir_depth
        self.timeout = timeout
        self.max_try_count = max_try_count
        self.req = requests.Session()
        self.req.headers = {
            'User-Agent': 'dotdotdown/{0}'.format(__version__),
            'Accept': '*/*',
        }
        self.download_files = []
        self.current_depth = 0

        if conf.proxy_socks:
            self.req.proxies = {
                'http': conf.proxy_socks,
                'https': conf.proxy_socks
            }

        self.__verify()

    def __verify(self):
        """

        """
        _urlparse = urlparse.urlparse(self.url)

        if _urlparse.scheme not in ('https', 'http') and _urlparse.netloc:
            raise Exception('The entered url address is invalid, detail: {0}'.format(self.url))

        if self.output_dir.startswith('./') or not self.output_dir.startswith('/'):
            self.output_dir = os.path.join(paths.ROOT_PATH, self.output_dir, _urlparse.netloc)

        if not os.path.isdir(self.output_dir):
            os.makedirs(self.output_dir)

        if conf.proxy_socks:
            # test google
            resp = self.req.get('https://www.google.com/')
            if resp.status_code != 200 and resp.url != 'https://www.google.com/':
                raise Exception('Test network proxy failed, please check proxy address：{0}'.format(conf.proxy_socks))

    def connect(self, url, method='get', timeout=None, max_try_count=None):
        """

        :param url:
        :param method:
        :param timeout:
        :param max_try_count:
        :return:
        """
        timeout = timeout or self.timeout
        max_try_count = max_try_count or self.max_try_count
        for i in range(1, max_try_count+1):
            try:
                return self.req.request(method, url, timeout=timeout, verify=False)
            except requests.exceptions.ReadTimeout as ex:
                logger.error('Connection timed out, wait 0.5s after the {0} attempt to connect ...'.format(i))
                time.sleep(0.5)
                if i == max_try_count:
                    raise ex

    def get_detect_content_type(self, url=None):
        """
        :param url:
        :return:
        """
        logger.debug('Start testing "{0}" url ...'.format(url))
        resp = self.connect(url, 'head')
        if resp.status_code == 200:
            if 'content-type' in resp.headers and resp.headers['content-type'].startswith('text/html'):
                return 'dir'
            else:
                return 'file'
        else:
            logger.error('[-] url:"{1}" , status code:{0}'.format(url or self.url))
            return None

    def get_url(self, url=None, output_dir=None):
        """

        :param url:
        :param output_dir:
        :return:
        """

        if self.dir_depth > 0 and self.current_depth > self.dir_depth:
            logger.warning("More than the maximum depth, current depth:{0}".format(self.current_depth))
            return None

        self.current_depth += 1

        #logger.debug('dir_depth: {0}, current_depth: {1} '.format(self.dir_depth, self.current_depth))

        query_url = url or self.url
        logger.info('Start analyzing {0} ...'.format(query_url))

        save_local_path = output_dir or self.output_dir
        resp = self.connect(query_url)

        if resp.status_code == 200:
            if not resp.content:
                logger.warning('[-] "{0}" content returns empty!'.format(query_url))
                return None

            html = lxml.html.fromstring(resp.content)
            links = html.findall('.//a')
            logger.debug('Found {0} a tag links and started parsing links...'.format(len(links)))
            for a in links:
                href = a.get('href')
                text = a.text

                if urllib.unquote_plus(href) == text:
                    sub_url = '{0}/{1}'.format(query_url, href)
                    uri_type = self.get_detect_content_type(sub_url)
                    output_dir = '{0}/{1}'.format(save_local_path, text)
                    if uri_type == 'dir':
                        if not os.path.isdir(output_dir):
                            os.makedirs(output_dir)
                            logger.debug('Create "{0}" directory successfully'.format(output_dir))
                        self.get_url(sub_url, output_dir)
                    if uri_type == 'file':
                        self.download_files.append(Link(
                            herf=a.get('href'),
                            text=a.text,
                            url=sub_url,
                            parent_url=query_url,
                            uri_type=uri_type,
                            save_local_path=output_dir
                        ))
                        if not os.path.isfile(output_dir):
                            download = self.connect(query_url)
                            with open(output_dir, "wb") as fp:
                                fp.write(download.content)
                            logger.info('[+] Save "{0}" file successfully'.format(output_dir))
                        else:
                            logger.warning('[-] "{0}" file already exists!!!'.format(output_dir))
            # TODO Directory depth multiple level issues

        else:
            logger.error('[-] url:"{1}" , status code:{0}!'.format(query_url))
            return None

    def start(self):
        """

        :return:
        """
        self.get_url()

        # TODO proxychains4 download method
