#!/usr/bin/env python3
""" Alta3 Research | Rob Womble
    lab 24 challenge: use for loops to display contents of a list of dictionaries
    -2nd attempt-"""

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

for farm in farms:  #iterate each dictionary
    item = ", ".join(farm["agriculture"]) #change list to useable string
    print(f"{farm['name']} produces the following: {item}") #disply which items are at each farm
