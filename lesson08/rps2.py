import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

playagain = True

while playagain:
    picks = ["Rock", "Paper", "Scissors"]
    playerchoice = input("Enter...\n1 for Rock,\n2 for Paper,\n3 for Scissors: \n\n")
    player = int(playerchoice)
    computerchoice = random.choice("123")
    computer = int(computerchoice)
    print("")
    if player < 1 | player > 3:
        sys.exit("You must enter a value between 1-3.")
    else:
        print("")
        print("You chose " + str(RPS(player)).replace('RPS.','') + ".")
        print("Python chosen " + str(RPS(computer)).replace('RPS.','') + ".")
        print("")   
    
    if picks[player - 1] == "Rock" and picks[computer - 1] == "Rock" or picks[player - 1] == "Paper" and picks[computer - 1] == "Paper" or picks[player - 1] == "Scissors" and picks[computer - 1] == "Scissors":
        print("No one wins!")
    elif picks[player - 1] == "Rock" and picks[computer - 1] == "Paper" or picks[player - 1] == "Paper" and picks[computer - 1] == "Scissors" or picks[player - 1] == "Scissors" and picks[computer - 1] == "Rock":
        print("You lose!")
    elif picks[player - 1] == "Rock" and picks[computer - 1] == "Scissors" or picks[player - 1] == "Paper" and picks[computer - 1] == "Rock" or picks[player - 1] == "Scissors" and picks[computer - 1] == "Paper":
        print("You win!")
    else:
        sys.exit("Error: Unexpected value.")   
    playagain = input("\nPlay again? \nY for Yes or \nQ to Quit \n\n")
    if playagain.lower() == "y":
        continue
    else:
        print("\n🎉🎉")
        print("Thank you for playing!\n")
        playagain = False
        break

sys.exit("Bye!")