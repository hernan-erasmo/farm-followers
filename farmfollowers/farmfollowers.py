# -*- coding: iso-8859-1 -*-
"""
This module contains the bulk of farm-followers
"""

import requests

from bs4 import BeautifulSoup


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
