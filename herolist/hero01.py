#!/usr/bin/env python3

heroes=  {
"wolverine":
    {"real name": "James Howlett",
    "powers": "regeneration",
    "archenemy": "Sabertooth",},

"harry potter":
    {"real name": "Harry Potter",
    "powers": "he's a wizard",
    "archenemy": "Voldemort",},

"agent fitz":
    {"real name": "Leopold Fitz",
    "powers": "intelligence",
    "archenemy": "Hydra",}        }

while True:
    char_name = input("Which character do you want to know about? (Wolverine, Harry Potter, Agent Fitz)").lower()
    if char_name in ("wolverine", "harry potter", "agent fitz"):
        break
    else:
        print("Invalid input. Please choose one of the characters from the list provided.")

while True:
 char_stat = input(' What statistic do you want to know about? (real name, powers, archenemy)').lower()
      if char_stat not in ('real name', 'powers', 'archenemy'):
          print("Invalid input. Please choose one of the characters from the list provided.")
        else:
            break

print(char_name.title() +"\'s " + char_stat + " is : "+ heroes[char_name][char_stat])

