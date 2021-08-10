#!/usr/bin/env python3
# NDE Challenge #3 - Dictionaries

# Use the following dictionary

pets = {"cats": ["fluffy", "snowball", "garfield"], "dogs": ["toto", "kujo", "spot"]}

# print out the following sentence - NOTE - {} are to show WHAT should be formatted in

# I have the {cats} {fluffy}, {snowball}, and {garfield}, and the {dogs} {toto}, {kujo}, and {spot}.

print(f"I have the {pets.keys()[0]} {pets['cats'][0]}, {pets['cats'][1]}, and  {pets['cats'][2]")
