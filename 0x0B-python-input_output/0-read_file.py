#!/usr/bin/python3
"""
Nothing imported here
"""


def read_file(filename=""):
	"""
	function that returns a file
	"""

	with open(filename, encoding = "UTF8") as file:
		file_content = file.read()
		print(file_content)
