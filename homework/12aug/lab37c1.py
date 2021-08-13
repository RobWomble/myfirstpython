#!/usr/bin/env python3
"""
I have tried putting .lower methods in various places.
Apparently either os or fnmatch don't like that.
The error says expected str or os object, not builtin method.
Even though the method should output a string!?
I finally tried the regex formatting below.  No error messages, but I can't get it to work.
I'm giving up.  It shouldn't take me a whole hour to do 1/6 of my homework.
"""

import os
import fnmatch

EXCLUDE = ["/usr", "/var"]


def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path, topdown=True):
        if root in EXCLUDE:
            dirs[:] = []
            files[:] = []
        for name in files:
            #A google search gave me the following.
            #I don't think the five minutes we spent on regex is enough to code with it.
            if fnmatch.fnmatch("(?i)" + name, "(?i)" + pattern):
                result.append(os.path.join(root, name))
    return result


def main():
    lookfor = input("What pattern am I looking for (Example: *.txt or *.cfg) ")
    lookwhere = input("What is the path in which I should search? ")
    print("Results: ", find(lookfor, lookwhere))


main()
