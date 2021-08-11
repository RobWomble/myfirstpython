#!/usr/bin/env python3
""" I've started ignoring the naming conventions on the labs to save time. """

import uuid

howmany = int(input("How many UUIDs should be generated? "))

print("Generating UUIDs...")
for rando in range(howmany):
    print( uuid.uuid4() )
