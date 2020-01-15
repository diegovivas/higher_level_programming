#!/usr/bin/python3
""" fetches starwars api """

import requests
import sys

if __name__ == "__main__":
    palabra = 'https://swapi.co/api/people' + '?search=' + sys.argv[1]
    fetch = requests.get(palabra)
    page = fetch.json()
    print('Number of results: ' + str(len(page['results'])))
    for element in page['results']:
        print(element['name'])
