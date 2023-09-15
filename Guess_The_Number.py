from random import randint
logo ="""

   ______                        ________            _   __                __             
  / ____/_  _____  __________   /_  __/ /_  ___     / | / /_  ______ ___  / /_  ___  _____
 / / __/ / / / _ \/ ___/ ___/    / / / __ \/ _ \   /  |/ / / / / __ `__ \/ __ \/ _ \/ ___/
/ /_/ / /_/ /  __(__  |__  )    / / / / / /  __/  / /|  / /_/ / / / / / / /_/ /  __/ /    
\____/\__,_/\___/____/____/    /_/ /_/ /_/\___/  /_/ |_/\__,_/_/ /_/ /_/_.___/\___/_/     
                                                                                          

"""

print(logo)

#Set user difficulty
def difficulty_setting():
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if difficulty == 'easy':
    return 10
  elif difficulty == 'hard' :
    return 5
  else:
    print("Improper input difficulty set to extreme.") 
    return 2

#Check the users guess against actual answer
def checkguess(guess):
  global OngoingGame
  if guess == correctnumber:
    print("Correct")
    OngoingGame = False
    return 
  elif guess > correctnumber:
    print("Too high")
    return turns-1
  else:
    print ("Too low")
    return turns-1
  

OngoingGame = True
correctnumber = randint(1, 100)
print("Welcome to the Number Guessing Game! ")
print("I'm thinking of a number between 1 and 100.")
print(correctnumber)
turns = difficulty_setting()

while OngoingGame:
  print(f"You have {turns} attempts remaining to guess the number.")
  guess = int(input("Make a guess: "))
  turns = checkguess(guess)
  if turns == 0:
    print("Out of guesses. Game over")
    OngoingGame = False
