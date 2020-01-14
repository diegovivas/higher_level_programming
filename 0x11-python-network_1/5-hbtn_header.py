#!/usr/bin/python3
""" fetches https://intranet.hbtn.io/status """

import requests
import sys

if __name__ == "__main__":
    fetch = requests.get(sys.argv[1])
    page = fetch.headers['X-Request-Id']
    print(page)
