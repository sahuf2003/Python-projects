import random
from replit import clear

def guess_number():
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 to 100")
  number = random.randint(1,100)
  return number

guess = guess_number()


def difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return 10
  elif level =="hard":
    return 5
def attempt():
  attempts = difficulty()
  print(f"You have {attempts} attempts remaining to guess the number.")
  while attempts > 0:
    user = int(input("Make a guess: "))
    if user == guess:
      print(f"You got it! The answer was {guess}")
      attempts = 0
    elif user > guess:
      print("Too high.")
      attempts -= 1
      print(f"You have {attempts} left to guess the number.")
    elif user < guess:
      print("Too low.")
      attempts -= 1
      print(f"You have {attempts} left to guess the number.")

def game():
   attempt()
   choice = input("Do you want to play again? Type 'y' or 'n': ")
   if choice == "y":
     clear()
     guess_number()
     game()
   else:
    print("Goodbye")
game()
