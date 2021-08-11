#!/usr/bin/env python3
linefile = input("enter file name: ")
## create file object in "r"ead mode
with open("linefile", "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()
    linenum = 0
    for line in configfile:
        linenum += 1
    
## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist, "\n", linenum)
