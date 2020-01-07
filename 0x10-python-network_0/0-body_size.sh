#!/bin/bash
#displays the size of the body of the response
curl -size 0.0.0.0:5000 | grep Content-Length:  |cut -d ' ' -f 2
