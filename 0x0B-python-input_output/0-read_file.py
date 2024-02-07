#!/usr/bin/python3
"""
<<<<<<< HEAD
Nothing imported
"""


def read_file(filename=""):
    """
    function that opens a file
    """

    with open(filename, encoding='utf-8') as f:
        f_contents = f.read()
        print(f_contents, end=' ')
        if __name__ == "__main__":
            read_file("my_file_0.txt")
=======
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
>>>>>>> ab0c00de4f8f1342c198ed45e9a00a39b518f76a
