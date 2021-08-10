#!/usr/bin/env python3

ipchk = input("Enter an ip address: ")

if ipchk == "192.168.70.1":
    print(f"Gateway address set: {ipchk} - Please run command again and select new address")
elif ipchk:
    print(f"The ip address was set: {ipchk}")
else:
    print("You did not provide input.")
