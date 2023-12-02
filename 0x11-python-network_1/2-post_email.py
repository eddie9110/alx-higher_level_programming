#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8)"""

import urllib.parse as parse
import urllib.request as request
import sys
import urllib.parse as parse

url = sys.argv[1]
email = sys.argv[2]

data = parse.urlencode({"email": email}).encode("ascii")
url_ = request.Request(url, data)
with request.urlopen(url_) as result:
    print(result.read().decode("utf-8"))
