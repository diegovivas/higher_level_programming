#!/usr/bin/python3
""" fetches https://intranet.hbtn.io/status str version"""

import requests

if __name__ == "__main__":
    fetch = requests.get('https://intranet.hbtn.io/status')
    page = fetch.text
    print("Body response:")
    print("\t- type: " + str(type(page)))
    print("\t- content: " + str(page))
