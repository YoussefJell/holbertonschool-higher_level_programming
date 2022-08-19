#!/usr/bin/python3
"""2-post_email Module"""
import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    my_val = urllib.parse.urlencode({'email': argv[2]}).encode('ascii')
    url = argv[1]
    req = urllib.request.Request(
        url, my_val, method='POST')
    with urllib.request.urlopen(req) as my_url:
        html = my_url.read()
        print(html.decode('utf-8'))
