#!/usr/bin/python3
"""4-hbtn_status Module"""
import requests
from sys import argv

if __name__ == "__main__":

    if len(argv[1]) == 1:
        myobj = {'q': argv[1]}
    else:
        myobj = {'q': ""}

    url = 'http://0.0.0.0:5000/search_user'
    try:
        r = requests.post(url, myobj).json()
        if r.get('id') and r.get('name'):
            print('[{}] {}'.format(
                r.get('id'), r.get('name')))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
