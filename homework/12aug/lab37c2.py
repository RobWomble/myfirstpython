#!/usr/bin/env python3


import os 
import fnmatch
import sys

EXCLUDE = ["/usr", "/var"] 


def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path, topdown=True):
        if root in EXCLUDE: 
            dirs[:] = [] 
            files[:] = [] 
        for name in files: 
            if fnmatch.fnmatch(name, pattern): 
                result.append(os.path.join(root, name)) 
    return result 

def main():
    lookfor = sys.argv[1]     #no way it's this simple
    lookwhere = sys.argv[2]   #holy moly, it is
    print("Results: ", find(lookfor, lookwhere)) 

main()
