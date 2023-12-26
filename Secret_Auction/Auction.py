from replit import clear

from art import logo
print(logo)
gameover = False
while not gameover:
  name = input("What is your name? ")
  bid = int(input("What is your bid? "))
  bidders = {}
  bidders[name] = bid
  print(bidders)
  other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")
  clear()
  if other_bidders == "no":
    gameover = True

def highest_bidder(bidders):
  highest_bid = 0
  for key in bidders:
    if bidders[key] > highest_bid:
      highest_bid = bidders[key]
      highest_bidder = key
  print(f"The winner is {highest_bidder} with ${highest_bid}")

highest_bidder(bidders)
