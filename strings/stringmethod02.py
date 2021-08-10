#!/usr/bin/env python3
""" Alta3 Research || Author: Rob Womble """

def main():
    """ runtime code """
    # create string
    lilstring = "Alta3 Research offers classes on Python coding"
    newlist = lilstring.split(" ") #convert to list
    print(newlist)

    #create list
    myiplist = ["192", "168", "0", "12"]
    singleip = ".".join(myiplist) #join with dots
    print(singleip)

# call main function
main()
