#!/usr/bin/python3
""" fetches github api """

import requests
import sys

if __name__ == "__main__":
    palabra = 'https://api.github.com/repos/'
    palabra = palabra + sys.argv[1] + '/' + sys.argv[2] + '/commits'
    fetch = requests.get(palabra)
    page = fetch.json()
    cont = 0
    for element in page:
        print("{}: {}".format(element['sha'],
                              element['commit']['committer']['name']))
        cont += 1
        if cont == 10:
            break
