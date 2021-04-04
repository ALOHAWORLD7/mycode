#!/usr/bin/python3

from random import randint


# Replace RPG starter project with this code when new instructions are live




def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : 'key'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : 'monster',
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : 'potion',
                  'north' : 'Pantry',
               },
            'Garden' : {
                  'north' : 'Dining Room'
               },
            'Pantry' : {
                  'south' : 'Dining Room',
                  'item' : 'cookie',
            }
         }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
 
  #when the player is in kitchen with monster
  if currentRoom == 'Kitchen' and 'monster' in rooms[currentRoom]['item']:
      print("About time... I was about to cook but looks like I have someone here to cook for me? HA HA HA HA...")
      print("If you would like to survive this stage, you have two oprions to choose from: \n 1. RUN \n 2. Cook \n Make a wise decision. GOOD LUCK!")
      #.lower() for case-sensitive
      action = input().lower()

      print("\n----------------------------------------")

      if action == 'run':
          print("Yo HighSpeed, you think you can outrun THE MONSTER and survive this stage???? Bruhhhh... let\'s see if you will survive...")
          #creating a random time in seconds for the player to escape
          run_away = randint(0, 10) 
          print(f"You took {run_away} seconds to run away.")
              
          if run_away >= 7:
              print (f"You were too slow to escape. You are now dead. You took {run_away} seconds.")
              print("Game Over")
              break 
          elif run_away >= 3:
              print(f"Yo HighSpeed, piece of advise to you - you better start doing more cardio ... Your run time wasn't that great. You took {run_away} seconds to run away.  You barely survived. Anyhoo, good luck for next stage.")
              #player will be automatically transferred to Dining Room.
              currentRoom = 'Dining Room'
              print("Now, you are in Dining Room.")
              
          else: 
              #if the run_away time is < 3, then player will be automatically placed in Dining room.
              print(f"YOU SURVIVED. You esacped in {run_away} seconds. That\'s awesome.")
              currentRoom = "Dining Room"
              print("Now, you are in Dining Room.")
      if action == 'cook':
          print("You will now be cooking for THE MONSTER. Ensure it tastes good otherwise you know what will happen to you...")
          playerResponse1 = input("Monster: Do you know how to cook? \n Enter y or n: \n").lower()
          #asking for response from player if he/she can cook or not
          if playerResponse1 == 'y':
              print("Monster: I need you to cook steak for me. Medium rare, please.")
              cook_quality = randint(1,3)
              if cook_quality == 1:
                  print("Monster: Steak was cooked to perfection. I will let you go this time.\n You SURVIVED!")
                  currentRoom = 'Dining Room'
                  print("Now, you are in Dining Room.")
              else:
                  print("You burnt my steak. That was the last piece I had. You are done.")
                  print('You were killed by THE MONSTER. Make sure you learn how to cook Steak and try again.  GAME OVER.')
                  break

  ## Define how a player can win
  #when a player is  in Garden with key and potion
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
    break

  ## If a player enters a room with a monster
  #elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
   # print('A monster has got you... GAME OVER!')
  elif currentRoom == 'Garden' and 'key' not in inventory and 'potion' not in inventory:
    print('You were not able to escape the house with the ultra rare key and magic potion... YOU LOSE! GAME OVER!')  
    break

