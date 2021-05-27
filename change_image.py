#!/usr/bin/env python3

""" Iterate through each file in the folder
For each file:
Size: Change image resolution from 3000x2000 to 600x400 pixel
Format: Change image format to .JPEG
"""

import sys
import os
from PIL import Image

directory = input("please insert here the directory where you store the images to convert: (full path)")
new_dir = input("please insert here the directory where you store the converted images: (full path)")

#check if new_dir exist, if it doesn't create one
if not os.path.exists(new_dir):
    os.makedirs(new_dir)

#iterate trough directory and convert images
for infile in os.listdir(directory):
    f, e = os.path.splitext(infile)
    outfile = new_dir + f +".jpeg"
    if infile != outfile: 
        try:
            with Image.open(directory + infile) as im:
                im.resize((600,400)).convert("RGB").save(outfile, "JPEG")
            im.close
            print("Converted {} to {}".format(infile, f+ ".jpeg"))
        except OSError:
            print("cannot convert", infile)        