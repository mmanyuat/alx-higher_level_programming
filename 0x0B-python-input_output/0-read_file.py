#!/usr/bin/python3
"""
Nothing imported here
"""
def read_file(filename=""):
	"""
	function that returns a file
	"""

	with open(filename, encoding = 'utf8') as file:
		file_content = file.read()
		print(file_content, end=' ')
		
if __name__ == "__main__":
    read_file("my_file_0.txt")
