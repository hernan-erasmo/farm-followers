# -*- coding: iso-8859-1 -*-

import os
import unittest
from farmfollowers import farmfollowers


class TestAccountsFileNeeded(unittest.TestCase):

	def setUp(self):
		with open('tmp_test_file.txt', 'w') as test_file:
			test_file.write('cnn\n')
			test_file.write('foxnews\n')
			test_file.write('@nytimes\n')
			test_file.write('\n')
			test_file.write('washingtonpost\n')

	def tearDown(self):
		os.remove('tmp_test_file.txt')

	def test_load_from_file_loads_all_accounts(self):
		accs = ['cnn', 'nytimes', 'foxnews', 'washingtonpost']
		ff = farmfollowers.FarmFollowers()
		ff.load_from_file('tmp_test_file.txt')
		
		self.assertSetEqual(set(accs), set(ff.accounts))

	def test_load_from_file_removes_at_character(self):
		ff = farmfollowers.FarmFollowers()
		ff.load_from_file('tmp_test_file.txt')

		for acc in ff.accounts:
			self.assertTrue('@' not in acc)
