rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
game_images = [rock, paper, scissors]
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user])
comp = random.randint(0,2)

print(f"computer chose:\n {game_images[comp]}")
if user == 0 and comp == 0:
  print("Draw")
elif user == 1 and comp == 1:
  print("Draw")
elif user == 2 and comp == 2:
  print("Draw")
elif user == 0 and comp == 2:
  print("You win")
elif user == 1 and comp == 0:
  print("You win")
elif user == 2 and comp == 1:
  print("You win")
else:
  print("You lose")
