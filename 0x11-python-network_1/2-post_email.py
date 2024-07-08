#!/usr/bin/python3
import urllib.parse
import urllib.request
import sys
"""
Modules first to parse the data
second to fetch the url
third to get the arguments
"""

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('ascii')
    with urllib.request.urlopen(url, data=data) as response:
        print(response.read().decode('utf-8'))
