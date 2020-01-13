#!/usr/bin/python3
""" fetches https://intranet.hbtn.io/status """

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as fetch:
        page = fetch.read()
        print("Body response:")
        print("\t- type: " + str(type(page)))
        print("\t- content: " + str(page))
        print("\t- utf8 content: " + page.decode('utf-8'))
