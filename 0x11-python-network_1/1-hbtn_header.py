#!/usr/bin/python3
import urllib.request
import sys
"""
the first module is meant to fetch the url
the second module fetches argument
"""

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.headers.get('X-Request-Id'))
