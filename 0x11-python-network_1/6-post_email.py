#!/usr/bin/python3
""" fetches https://intranet.hbtn.io/status """

import requests
import sys

if __name__ == "__main__":
    myobj = {'email':sys.argv[2]}
    fetch = requests.post(sys.argv[1], data = myobj)
    print(fetch.text)
