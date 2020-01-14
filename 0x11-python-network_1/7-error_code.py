#!/usr/bin/python3
""" fetches https://intranet.hbtn.io/status """

import requests
import sys

if __name__ == "__main__":
    fetch = requests.get(sys.argv[1])
    answer = fetch.text
    if fetch.status_code is not 200:
        print('Error code: ' + str(fetch.status_code))
    else:
        print(answer)
