## CS160 Example: Guess the Number
## August 2022
## J. Abramson

## We need math to compute the log (base 2)
## We need random so the computer can pick a secret number
##
import math
import random

## The range of the number being guessed
## The target is the max number of guesses that it should take
## if the guesser is doing an optimal job.
##
LIMIT = 1000
TARGET = math.ceil(math.log(LIMIT,2))

def userGuesses():

  print("Hello, I have picked a number between 1 and", LIMIT)
  print("You get to try to guess it, hopefully in", TARGET, "guesses or less!")

  secret = random.randint(1,LIMIT)
  numGuesses = 0
  
  while(True):
    numGuesses = numGuesses + 1
    guess = int(input("Enter your guess: "))
    if (guess < secret):
      print("Your guess is too low, try again")
    elif (guess > secret):
      print("Your guess is too high, try again")
    else:
      print("Nice work!  You got it in ", numGuesses, "guesses!")
      break

def computerGuesses():

  print("Hello, please pick a number between 1 and", LIMIT)
  print("I will guess it in", TARGET, "guesses or less!")

  numGuesses = 0
  low = 1
  high = LIMIT
  while(True):
    numGuesses = numGuesses + 1
    guess = low + int((high-low)/2)
    print("My guess is", guess)
    feedback = int(input("Enter 1 for too low, 2 for too high, or 3 for just right!"))
    if (feedback == 1):
      low = guess
    elif (feedback == 2):
      high = guess
    else:
      break

  print("Congratulations to me, took me", numGuesses, "guesses!  Can you do better?")


def main():
  print("Welcome!")
  print("  1: I guess")
  print("  2: You guess")
  option = int(input("Please pick the option (1 or 2): "))
  if (option == 1):
    userGuesses()
  elif (option == 2):
    computerGuesses()
  else:
    print("Sorry, not a valid option!")

main()