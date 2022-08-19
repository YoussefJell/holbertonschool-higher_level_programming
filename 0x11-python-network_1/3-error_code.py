#!/usr/bin/python3
"""3-error_code Module"""
import urllib.request
import urllib.error
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(url) as my_url:
            html = my_url.read()
            print(html.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code: ' + e.code)
