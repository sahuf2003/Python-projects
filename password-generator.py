#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
pass_letters = ""
for letter in range(0,nr_letters):
  pass_letters+=(random.choice(letters))
for digit in range(0,nr_numbers):
  pass_letters+=(random.choice(numbers))
for symbol in range(0,nr_symbols):
  pass_letters += (random.choice(symbols))
print(pass_letters)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbols, 2 number = g^2jk8&P
# lol = random.shuffle(pass_letters)
# print(lol)
arraye = list(pass_letters)
print(arraye)
random.shuffle(arraye)
print(arraye)
lol = ""
for damn in arraye:
  lol+=(damn)
print(lol)
#Password Generator Project


