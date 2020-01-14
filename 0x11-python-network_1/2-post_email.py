#!/usr/bin/python3
""" Post request """

import urllib
import sys
from urllib import request, parse

if __name__ == "__main__":
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    data = parse.urlencode(values)
    data = data.encode('ascii')
    req = request.Request(url, data)
    with urllib.request.urlopen(req) as fetch:
        page = fetch.read()
        print(page)
