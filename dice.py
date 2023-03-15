# this is the dice program

import random

print('You can roll a 4,6,8,10,12, 20, or 100 sided die.')

while True:
  print('What size die do you want to roll?')
  diceChoice = input()
  if diceChoice == '4':
    print('You rolled ' + str(random.randint(1, 4)) + '.')
  elif diceChoice == '6':
    print('You rolled ' + str(random.randint(1, 6)) + '.')
  elif diceChoice == '8':
    print('You rolled ' + str(random.randint(1, 8)) + '.')
  elif diceChoice == '10':
    print('You rolled ' + str(random.randint(1, 10)) + '.')
  elif diceChoice == '12':
    print('You rolled ' + str(random.randint(1, 12)) + '.')
  elif diceChoice == '20':
    print('You rolled ' + str(random.randint(1, 20)) + '.')
  elif diceChoice == '100':
    print('You rolled ' + str(random.randint(1, 100)) + '.')
  else:
    print('Try again.')
