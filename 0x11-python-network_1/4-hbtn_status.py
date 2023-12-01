#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests

response = requests.get('https://intranet.hbtn.io/status')
print(f"Body response:\n\t- type: {type(response.text)}\n\t- content: {response.text}")

