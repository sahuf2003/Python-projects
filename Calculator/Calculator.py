import art
from replit import clear
def add(n1,n2):
  return n1+n2

def sub(n1,n2):
  return n1 - n2

def mul(n1,n2):
  return n1 * n2

def div(n1,n2):
  return n1 / n2

def pow(n1,n2):
  return n1 ** n2

operations = {
  "+": add,
  "-": sub,
  "*": mul,
  "/": div,
  "**": pow
}
# operations["+"] = add
# operations["-"] = sub
# operations["*"] = mul
# operations["/"] = div
def calculator():
  print(art.logo)
  num1 = int(input("What's the first number?: "))
  
  
  for symbol in operations:
    print(symbol)
  should_continue = True
  while should_continue:
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = int(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    res = input(f"Type 'y' to continue calculating with {answer}, or start new calculaion ")
    if res == "y":
      num1 = answer
      clear()
    else:
      should_continue = False
calculator()
