#!/usr/bin/python3
"""1-hbtn_header Module"""
from urllib.request import urlopen
from sys import argv

if __name__ == "__main__":
    with urlopen(argv[1]) as my_url:
        headers = my_url.info()
        print(headers.get('X-Request-Id'))
