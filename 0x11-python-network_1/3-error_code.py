#!/usr/bin/python3
""" Post request """

import urllib
import sys
from urllib import request

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as fetch:
            data = fetch.read()
            html = data.decode('utf-8')
            print(html)

    except urllib.error.HTTPError as e:
        print('Error code: ' + str(e.code))
