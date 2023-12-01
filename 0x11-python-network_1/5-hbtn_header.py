#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and
displays the value of the variable X-Request-Id in the response header"""

from sys import argv
import requests

resp_onse = requests.get(argv[1])
print(resp_onse.headers.get('X-Request-Id'))
