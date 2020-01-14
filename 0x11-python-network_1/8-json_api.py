#!/usr/bin/python3
""" fetches https://intranet.hbtn.io/status """

import requests
import sys

if __name__ == "__main__":

    if len(sys.argv) > 1:
        myobj = {'q': sys.argv[1]}
    else:
        myobj = {'q': ""}
    fetch = requests.post('http://0.0.0.0:5000/search_user', data=myobj)
    try:
        ans = fetch.json()
        if len(ans) > 0:
            print("[{}] {}".format(ans.get('id'), ans.get('name')))
        else:
            print('No result')
    except:
        print("Not a valid JSON")
