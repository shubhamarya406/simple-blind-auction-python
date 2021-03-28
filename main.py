from replit import clear
from art import logo

print(logo)
print("Welcome to the secret auction program!!!")
choice="yes"
bidder={}
while choice.lower()=="yes":
  name=input("\nWhat is your name?:")
  bidder[name]=int(input("What is your bid?: $"))
  choice=input("Are ther any other bidders? Type 'yes' or 'no'.\n")
  if choice=="yes":
    clear()
max=0
winner=""
for i in bidder:
  if bidder[i]>=max:
    max=bidder[i]
    winner=i
clear()
print(f"The winner is {winner} with a bid of ${max}.")