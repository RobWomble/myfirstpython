#!/usr/bin/env python3

round = 0
answer = " "

while round < 3 and answer.title() != "Brian":
    round += 1
    answer = input('Finish the movie title: "Monty Python\'s The Life of _____": ')
    if answer.title() == "Brian":
        print("Correct!")
    elif answer.lower() == "shrubbery":
        print("You gave the super secret answer!")
        exit()
    elif round == 3:
        print("Sorry, the answer was Brian.")
    else:
        print("Sorry. Try again!")
