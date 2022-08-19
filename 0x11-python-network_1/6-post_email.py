#!/usr/bin/python3
"""4-hbtn_status Module"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    myobj = {'email': argv[2]}
    r = requests.post(url, data=myobj)
    print(r.text)
