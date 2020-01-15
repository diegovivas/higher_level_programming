#!/usr/bin/python3
""" fetches github api """

import requests
import sys

if __name__ == "__main__":
    palabra = 'https://api.github.com/user'
    fetch = requests.get(palabra, auth=(sys.argv[1], sys.argv[2]))
    page = fetch.json()
    if 'id' in page:
        print(page['id'])
    else:
        print('None')
