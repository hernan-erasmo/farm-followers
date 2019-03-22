# -*- coding: iso-8859-1 -*-

import requests

from bs4 import BeautifulSoup

class FarmFollowers:
	def __init__(self):
		self.accounts = []

	def load_from_file(self, filepath):
		"""
			Load accounts from file. Removes all @ characters and 
			removes all duplicates from the resulting list
		"""
		with open(filepath, 'r') as acc_file:
			for line in acc_file.readlines():
				if len(line.strip()) == 0:
					continue

				if '@' in line:
					line = line.replace('@', '')
				
				self.accounts.append(line.strip())

			self.accounts = list(set(self.accounts))


if __name__ == '__main__':
	pass