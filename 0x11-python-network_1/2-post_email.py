#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8)"""

import urllib.parse as parse
import urllib.request as request
import sys
import urllib.parse as parse

url_ = sys.argv[1]
email_ = sys.argv[2]
parsed_ = parse.urlencode({"email": email_}).encode("ascii")
data_ = request.Request(url_, parsed_)
with request.urlopen(data_) as r:
    print(r.read().decode("utf-8"))
