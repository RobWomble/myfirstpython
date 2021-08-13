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
    #for card in cards['cards']:
    #    print(card['name'])
    #    break

    with open(f"{setcode}.cardlist.txt", "w") as card_output:
        for card in cards['cards']:
            #the way I'm writing this string bothers me, 
            #but I'm in too much of a hurry to do it more cleanly
            print(f"Name: {card['name']}\nCombined mana cost: {card['cmc']}\nType: {card['types']}\nText: {card['text']}\n\n")

if __name__ == "__main__":
    main()
