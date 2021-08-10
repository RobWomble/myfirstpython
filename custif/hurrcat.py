#!/usr/bin/env python3
""" Alta3 Research | Rob Womble
    A script to determine hurricane category based on wind speed in mph"""

# Requesting user input for speed
speed = float(input("Enter current wind speed in mph: "))

# Using speed to determine category rating.
if speed > 156:
    category = "Five"
elif speed > 129:
    category = "Four"
elif speed > 110:
    category = "Three"
elif speed > 95:
    category = "Two"
elif speed > 73:
    category = "One"
else:
    print("You are not currently experiencing a hurricane.  Congratulations!")
    exit() #kill the script to avoid error when {category} isn't defined in final print statement 

#output answer to user with previously defined category
print(f"You are currently experiencing a Category {category} Hurricane. Seek immediate shelter.")
