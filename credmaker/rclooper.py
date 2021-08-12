#!/usr/bin/env python3
""" Alta3 Research | Rob Womble
    Generate a series of admin.rc files based on csv input """

import csv

with open("csv_users.txt", "r") as csvfile:                     #pull user data from file
    for row in csv.reader(csvfile):                             #iterate through rows
        filename = f"{row[3]}.admin.rc"                         #create a file based on username
        with open(filename, "w") as rcfile:                     #append necessary commands using pulled user data
            print("export OS_AUTH_URL=" + row[0], file=rcfile)
            print("export OS_IDENTITY_API_VERSION=3", file=rcfile)
            print("export OS_PROJECT_NAME=" + row[1], file=rcfile)
            print("export OS_PROJECT_DOMAIN_NAME=" + row[2], file=rcfile)
            print("export OS_USERNAME=" + row[3], file=rcfile)
            print("export OS_USER_DOMAIN_NAME=" + row[4], file=rcfile)
            print("export OS_PASSWORD=" + row[5], file=rcfile)

print("admin.rc files created!") #notify script user of success
