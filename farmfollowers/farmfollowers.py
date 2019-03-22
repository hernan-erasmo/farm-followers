# -*- coding: iso-8859-1 -*-
"""
This module contains the bulk of farm-followers
"""

import requests

from bs4 import BeautifulSoup

TWITTER_URL = 'https://www.twitter.com/'
STATUS_URL = TWITTER_URL + '{screen_name}' + '/status/' + '{status_id}'

class Status:
    """
        This class represents an individual Tweet, along with all
        the information that is gathered when parsed.
    """
    def __init__(self, *args, **kwargs):
        self.screen_name = None
        self.status_id = ''
        self.is_retweet = False
        self.status_text = ''
        self.favourited_by = []
        self.retweeted_by = []

        if 'screen_name' and 'status_id' in kwargs:
            self.screen_name = kwargs['screen_name']
            self.status_id = kwargs['status_id']


class FarmFollowers:
    """
        This class groups the functionallity of farm-followers
    """
    def __init__(self):
        self.accounts = []

    def load_from_file(self, filepath):
        """
            Load accounts from file. Removes all @ characters and
            removes all duplicates from the resulting list
        """
        with open(filepath, 'r') as acc_file:
            for line in acc_file.readlines():
                if not line.strip():
                    continue

                if '@' in line:
                    line = line.replace('@', '')

                self.accounts.append(line.strip())

            self.accounts = list(set(self.accounts))


if __name__ == '__main__':
    pass
