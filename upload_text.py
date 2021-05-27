#!/usr/bin/env python3
""" Iterate trhough a directory with .txt to elaborate .json format, and submit it
    Image associated will be already upload, just retrieved from the code (line 19)  
    need: sys[1] : directory with .txt
          sys[2] : url where to submit"""
import os
import requests
import sys

directory = sys.argv[1]
url =sys.argv[2]

for file in os.listdir(directory):
    if file.endswith(".txt"):
        with open(directory + file, "r") as f:
            lines = f.readlines()
            feed_dict = {
                "name":lines[0].rstrip(), 
                "weight":int("".join(c for c in lines[1] if c.isnumeric())), 
                "description":lines[2].rstrip(),
                "image_name": file[:file.index(".")] + str(".jpeg")
                }
            r = requests.post(url, data=feed_dict)
            r.raise_for_status()
            print("Uploading file : {}".format(file))

#print(feed_dict)        
