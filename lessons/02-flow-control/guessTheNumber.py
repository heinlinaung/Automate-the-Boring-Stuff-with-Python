# this is guessing game
import random
secretNum= random.randint(1,20)
print('I am thinking a number which I am guessing between 1 - 20. Guess it.')

# ask the player
for count in range(1,7):
  print('Take a guess.')
  guessNum = int(input())

  if guessNum<secretNum:
    print('Guess too low')
  elif guessNum > secretNum:
    print('Guess too high')
  else:
    break # guess correctly

if guessNum == secretNum:
  print('Good job, you guess correctly in ',count, ' tries.')
else:
  print('Nopeeeee. the guess number is ', secretNum)
