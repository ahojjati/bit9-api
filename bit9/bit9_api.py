#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Josh Maine'
__version__ = '1'
__license__ = 'GPLv3'

import requests


class Bit9Api():
    def __init__(self, user='', password='', data_format='json', proxies=None):
        self.baseurl = "https://services.bit9.com/CyberForensicsService/"
        self.user = user
        self.password = password
        self.flag = {'THREAT_TRUST': 1,
                     'FILE_INFO': 2,
                     'PE_HEADER_METADATA': 4,
                     'CERTIFICATE': 8,
                     'BASE_ALL': 15,
                     'CERTIFICATE_EX': 128,
                     'CATEGORY': 256}
        self.data_format = data_format
        self.proxies = proxies
        self.version = '1'
        self.tool = "pythonapi"

    @property
    def lookup_usageinfos(self):
        """

        :return:
        """
        url = self.baseurl + self.version + "/usageinfos/lookup." + self.data_format
        values = dict(username=self.user, password=self.password, tool=self.tool)

        try:
            response = requests.post(url, values, proxies=self.proxies)
        except Exception:
            return dict(error=Exception)

        if response.status_code == requests.codes.ok:
            return response.json()
        else:
            return dict(response_code=response.status_code)

    def lookup_md5(self, this_hash, flag=15):
        """

        :param this_hash:
        :param flag:
        :return:
        """
        url = self.baseurl + self.version + "/hashinfo/lookup." + self.data_format
        values = dict(username=self.user, password=self.password, md5=this_hash, flags=flag, tool=self.tool)

        try:
            response = requests.post(url, values, proxies=self.proxies)
        except Exception:
            return dict(error=Exception)

        if response.status_code == requests.codes.ok:
            return response.json()
        else:
            return dict(response_code=response.status_code)

    def lookup_batch_md5(self, hash_list, flag=15):
        """

        :param hash_list:
        :param flag:
        :return:
        """
        url = self.baseurl + self.version + "/hashinfos/lookup." + self.data_format
        values = dict(username=self.user, password=self.password, md5=hash_list, flags=flag, proxies=self.proxies,
                      tool=self.tool)
        try:
            response = requests.post(url, values, proxies=self.proxies)
        except Exception:
            return dict(error=Exception)

        if response.status_code == requests.codes.ok:
            return response.json()
        else:
            return dict(response_code=response.status_code)

    def _lookup_extended(self, this_hash, lookup_type):
        """

        :param this_hash:
        :param lookup_type:
        :return:
        """
        url = self.baseurl + self.version + lookup_type + "/lookup." + self.data_format
        values = dict(username=self.user, password=self.password, md5=this_hash, tool=self.tool)

        try:
            response = requests.post(url, values, proxies=self.proxies)
        except Exception:
            return dict(error=Exception)

        if response.status_code == requests.codes.ok:
            return response.json()
        else:
            return dict(response_code=response.status_code)

    def lookup_certificates(self, this_hash):
        """

        :param this_hash:
        :return:
        """
        return self._lookup_extended(this_hash, "/certificates")

    def lookup_files(self, this_hash):
        """

        :param this_hash:
        :return:
        """
        return self._lookup_extended(this_hash, "/files")

    def lookup_packages(self, this_hash):
        """

        :param this_hash:
        :return:
        """
        return self._lookup_extended(this_hash, "/packages")

    def lookup_scanresults(self, this_hash):
        """

        :param this_hash:
        :return:
        """
        return self._lookup_extended(this_hash, "/scanresults")