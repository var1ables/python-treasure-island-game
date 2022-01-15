#Introduction to the game
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#First choice, direction
direction = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right"').lower()

#wrong choice, game over
if direction == 'left':
  print('You fall into a hole, dying of embarassment. GAME OVER') 

#correct choice, game continues
elif direction == 'right':
  choice = input('You\'ve come to a lake. Type "wait" to wait for a boat, swim to try to swim across or walk to walk along the shore. You think you see a small island in the middle of the lake.').lower()
#options for the second choice

#Walking away from the game
  if choice == 'walk':
    print("You enjoy a nice walk around the lake. Who needs treasure anyway? GAME OVER")

#second choice for the more impatient  
  elif choice == 'swim':
    print("You forgot to learn the swim skill. You drown only a few moments before a boat comes and see you thrashing about. GAME OVER")

#Correct choice, waiting for the boat
  elif choice == 'wait':
    new_choice = input("A boat comes along and takes you to the island in the middle of the lake. Not far from shore is small village with three doors. Red Blue and Green. Choose one").lower()

#Wrong choice with gruesome result
    if new_choice == 'red':
      print("Behind the door is a vicious pirate gang. You are stabbed repeatedly by their long thin blades before you\'re tied to their flag pole as a warning to those who come to their village. GAME OVER")

#Wrong choice with gruesome result
    elif new_choice == 'blue':
      print('Behind the blue door are starving dogs, forgotten by their owners. They violently charge at you, knocking you down and gnawing at your every limp. You\'re torn to pieces by the hungry hounds leaving only your bones. GAME OVER')

#Correct choice and the end of the game
    elif new_choice == 'green':
      print('You\'ve discovered what you always dreamed of! A pirate\'s treasure chest full ill-gotten gains. You take as much as you carry back to the boat before you leave, never to return. Who knew it was so easy to become filthy rich?')

#Snarky end comments
  else:
      print("who do you think is writing this? I've got things to do I can't come up with every option. GAME OVER.")
else: 
    print("who do you think is writing this? I've got things to do I can't come up with every option. GAME OVER.")   