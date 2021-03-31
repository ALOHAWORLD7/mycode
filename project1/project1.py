#!/usr/bin/env python3

questions = [
        "Are there snakes in Hawai'i?","no",
        "How many official Islands are in Hawai'i?", "eight",
        "Does Hawai'i Observe Daylight Savings Time?", 'no',
        ]


funFacts  = 0
current = 0

while funFacts < 3:
    funFacts += 1
    userInput  = input(questions[current])
    if userInput.lower() == questions[current + 1]:
        print("There you go...")
        current += 2 
    elif funFacts == 3:
        print("This was your last attempt. Mahalo!")
        current += 2
    else:
        print("Wrong Answer")

print("I hope it was informative. Mahalo for playing along...")
