#!/usr/bin/env python3

import requests

API = "https://api.magicthegathering.io/v1/"

def main():

    setcode = input("What is the code of the set you are trying to lookup? ").lower()
    resp = requests.get(f"{API}cards?set={setcode}")
    cards = resp.json()

    # the following are how I took forever to parse the data structure
    #print(type(cards))
    #print(cards.keys())
    #print(type(cards['cards']))
    #print(cards['cards'][1].keys())
    #for card in cards['cards']:
    #    print(card['name'])
    #    break

    with open(f"{setcode}.cardlist.txt", "w") as card_output:
        for card in cards['cards']:
            # the way I'm writing this string bothers me, 
            # but I'm in too much of a hurry to do it more cleanly
            #
            # I wanted to add colors, but some cards don't have colors,
            # and I don't intend to figure out error-handling in an
            # f-string for an assignment that was due yesterday

            print(f"Name: {card['name']}\nCombined mana cost: {card['cmc']}\nType: {card['types']}\nText: {card['text']}\n\n", file=card_output)

if __name__ == "__main__":
    main()
# tested, and it works, finally.  In hindsight, it would have been a bit
# easier to test if I had used a smaller set.  I just picked the
# particular set that I did because I like one of the cards in it.
#
# fun fact: Shahrazad is one of only 3 cards that is banned by name from
#           tournament play in formats that allow cards that old.
