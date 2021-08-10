#!/usr/bin/env python3

speed = float(input("Enter current wind speed in mph: "))

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
    exit()

print(f"You are currently experiencing a Category {category} Hurricane. Seek immediate shelter.")
