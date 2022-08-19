#!/usr/bin/python3
"""10-my_github module"""
import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get(
        'https://api.github.com/repos/{0}/{1}/commits'.format(argv[2], argv[1])).json()

    for i in range(0, 10):
        print("{0}: {1}".format(r[i].get('sha'),
              r[i]['commit']['author']['name']))
