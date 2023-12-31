import random
import game_data
from game_data import data
from art import logo, vs
from replit import clear
def get_random_account():
  random_account = random.choice(data)
  return random_account

def compare_followers(account_a, account_b):
  if account_a['follower_count'] > account_b['follower_count']:
    return "A"
  else:
    return "B"
account_a = get_random_account()
score = 0
gameover = False
while not gameover:
  print(logo)
  account_b = get_random_account()
  print(f"Compare A: {account_a['name']}, {account_a['description']} from {account_a['country']}")
  print(vs)
  
  print(f"Compare B: {account_b['name']}, {account_b['description']} from {account_b['country']}")
  user_input = input("Who has more followers? Type 'A' or 'B': ").upper()
  clear()
  print(logo)
  if user_input == compare_followers(account_a, account_b):
    score += 1
    print(f"You're right! Current score: {score}.")
  else:
    print(f"Sorry, that's wrong. Final score: {score}")
    score = 0
  if score == 0:
    gameover = True
  elif score > 0:
    account_a = account_b
