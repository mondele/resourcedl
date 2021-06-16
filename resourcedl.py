#!/home/jdwood/anaconda3/bin/python
# coding=<UTF-8>

#version 0.1
# by John Wood -- for Tech Advance
#Import necessary python components

import os	# file system commands
import os.path # commands to handle paths
import re	# regular expressions
import sys	# command line arguments
import shutil	# high level file operations
import yaml
import sqlite3
import platform

class machine:
    def __init__(self, theOS, happyPath):
        self.theOS = theOS
        self.happyPath = happyPath

thisPlat = platform.platform()
if("Linux" in thisPlat):
    thisOne = machine("linux","~/.config/BTT-Writer/library/")
elif ("Darwin" in thisPlat):
    thisOne = machine("macos","~/Library/Application Support/BTT-Writer/library/")
elif ("Windows" in thisPlat):
    thisOne = machine("windows","%localappdata%\BTT-Writer\library\")
    else sys.exit("Unsupported or unrecognized computer platform")

theIndex = thisOne.happyPath + "index.sqlite"

myconnection = sqlite3.connect(theIndex)

mydb = myconnection.cursor()

for row in mydb.execute("SELECT url FROM resource_format"):
    print(row[0])

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

