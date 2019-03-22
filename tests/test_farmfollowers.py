# -*- coding: iso-8859-1 -*-
"""
This module contains tests for the FarmFollowers class
"""

import os
import unittest
from farmfollowers.farmfollowers import FarmFollowers


class TestAccountsFileNeeded(unittest.TestCase):
    """
        This class groups unit tests that need to create
        and populate a file in order to run.
    """

    def setUp(self):
        """
            Unit test setup. Runs before every test.
        """
        with open('tmp_test_file.txt', 'w') as test_file:
            test_file.write('cnn\n')
            test_file.write('foxnews\n')
            test_file.write('@nytimes\n')
            test_file.write('\n')
            test_file.write('washingtonpost\n')

    def tearDown(self):
        """
            Unit test tear down. Runs after every test.
        """
        os.remove('tmp_test_file.txt')

    def test_load_from_file_loads_all_accounts(self):
        """
            Test that all accounts listed inside the input file
            are loaded.
        """
        accs = ['cnn', 'nytimes', 'foxnews', 'washingtonpost']
        farm_followers = FarmFollowers()
        farm_followers.load_from_file('tmp_test_file.txt')

        self.assertSetEqual(set(accs), set(farm_followers.accounts))

    def test_load_from_file_removes_at_character(self):
        """
            Test that the @ character is not present on any loaded
            account.
        """
        farm_followers = FarmFollowers()
        farm_followers.load_from_file('tmp_test_file.txt')

        for acc in farm_followers.accounts:
            self.assertTrue('@' not in acc)
