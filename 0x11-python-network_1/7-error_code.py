#!/usr/bin/python3
""" Python script that takes in a URL, sends a request
to the URL and displays the body of the response """

import requests
import requests

resp_onse = requests.get(argv[1])

if resp_onse.status_code > 400:
    print("Error code:", resp_onse.status_code)
else:
    print(resp_onse.text)
