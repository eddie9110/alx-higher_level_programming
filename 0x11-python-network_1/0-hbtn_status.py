#!/usr/bin/python3
"""python script that fetches https://alx-intranet.hbtn.io/status"""

import urllib.request
with urllib.request.urlopen("https://intranet.hbtn.io/status") as webpage_result:
    web_page = webpage_result.read()
    print(f"Body response:\n\t- type: {type(web_page)}\n\t- content: {web_page}\n\t\
- utf8 content: {web_page.decode('utf-8')}")
