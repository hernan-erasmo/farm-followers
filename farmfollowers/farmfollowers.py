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
    def __init__(self, **kwargs):
        self.screen_name = None
        self.status_id = ''
        self.is_retweet = False
        self.status_text = ''
        self.favourited_by = []
        self.retweeted_by = []

        if 'screen_name' and 'status_id' in kwargs:
            self.screen_name = kwargs['screen_name']
            self.status_id = kwargs['status_id']
            self._get_status_data()

    def _get_status_data(self, **kwargs):
        """
        GETs this status information from Twitter website and populates
        this Status data fields.
        """
        req = requests.get(STATUS_URL.format(
            screen_name=kwargs['screen_name'], status_id=kwargs['status_id']))

        soup = BeautifulSoup(req.content, 'html.parser')
        status_container = soup.find(
            'div',
            {'class':['permalink-inner permalink-tweet-container']}
        )

        self.status_text = status_container.find(
            'div',
            {'class':'js-tweet-text-container'}
        ).text.strip()


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
