from art import logo
import random

print(logo)

number = random.randint(1, 101)
print("Welcome to the number guessing game")
level = input("Type e for easy or h for hard level:")
if level == "e":
  attempts = 10
elif level == "h":
  attempts = 5

the_end = False

while the_end != True:
  guess = int(input("Guess a number: "))
  if guess > number:
    print("To high")
  elif guess < number:
    print("Too low")
  elif guess == number:
    print(f"You found the number: {number}")
    the_end == True
  attempts -= 1
  if attempts == 0:
    print("Game over, you ran out of attempts")
    the_end == True



