#!/usr/bin/env python3
""" Alta3 Research | Rob Womble
    11Aug2021 Homework 1
    Loop and print found items  """

def main():
    #collect user input, convert into list, use in sentence
    item_list = input('enter a list of items, separated by a space: ').title().split(' ')
    for item in item_list:
        print(f'{item} was found at the dog park.')
    print('Gee, you sure lose a lot of things at the dog park.')

main()
