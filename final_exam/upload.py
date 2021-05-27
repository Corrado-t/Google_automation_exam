#!/usr/bin/env python3

import os
import requests
import sys

# This example shows how a file can be uploaded using
# The Python Requests module
"""
with open('/usr/share/apache2/icons/icon.sheet.png', 'rb') as opened:
    r = requests.post(url, files={'file': opened})
"""
url ="http://localhost/upload/"
directory = sys.argv[1]

for file in os.listdir(directory):
    if file.endswith(".jpeg"):
        with open(directory + file, "rb") as f:
            r = requests.post(url, files={'file': f})
            r.raise_for_status()
        print("Uploading : {}".format(f))
            


