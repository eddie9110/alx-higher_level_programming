#!/usr/bin/python3
"""python script that fetches https://alx-intranet.hbtn.io/status"""

import urllib.request as request

with request.urlopen("https://alx-intranet.hbtn.io/status") as res:
    fet_ched = res.read()
    print("Body response:\n\t- type: {}\n\t- content: {}\n\t\
- utf8 content: {}".format(type(fet_ched), fet_ched, fet_ched.decode("utf-8")))
