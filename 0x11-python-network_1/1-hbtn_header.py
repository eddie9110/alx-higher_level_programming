#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response. """
import urllib.request as url_req
import sys

with url_req.urlopen(sys.argv[1]) as result:
    x_val = result.info()
    print(x_val.get("X-Request-Id"))
