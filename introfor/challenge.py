#!/usr/bin/env python3
""" Alta3 Research | Rob Womble
    lab 24 challenge: use for loops to display contents of a list of dictionaries """

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

for farm in farms:  #iterate each dictionary
    for harvestable in farm["agriculture"]:  #iterate each farm item 
        #display a line for each iteration of iteration, describing which items are at the farm
        print(f"{farm['name']} raises {harvestable}")
