#!/bin/bash
#sends a POST request to the URL
curl -s -d email=hr@holbertonschool.com -d subject="I will always be here for PLD" "$1"
