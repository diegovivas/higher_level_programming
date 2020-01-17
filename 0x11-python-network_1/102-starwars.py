#!/usr/bin/python3
""" fetches starwars api """

import requests
import sys

if __name__ == "__main__":
    palabra = 'https://swapi.co/api/people/' + '?search=' + sys.argv[1]
    fetch = requests.get(palabra)
    page = fetch.json()
    print('Number of results: ' + str((page['count'])))
    while (True):
        for element in page['results']:
            print(element['name'])
            for element2 in element['films']:
                fetch2 = requests.get(element2)
                page2 = fetch2.json()
                print("\t{}".format(page2['title']))
        if page['next'] is None:
            break
        fetch = requests.get(page['next'])
        page = fetch.json()
