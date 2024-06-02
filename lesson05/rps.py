import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

# print(RPS(2))
# print(RPS.ROCK)
# print(RPS['ROCK'])
# print(RPS.ROCK.value)

picks = ["Rock", "Paper", "Scissors"]

def playAgain():
    startagain = input("Play again? Y/N ")
    if startagain == "Y" or startagain == "y" or startagain == "Yes" or startagain == "yes":
        playGame()
    elif startagain == "N" or startagain == "n" or startagain == "No" or startagain == "no":
        sys.exit("Goodbye!")
    else: 
        playAgain()

def playGame():
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
        playAgain()
    elif picks[player - 1] == "Rock" and picks[computer - 1] == "Paper" or picks[player - 1] == "Paper" and picks[computer - 1] == "Scissors" or picks[player - 1] == "Scissors" and picks[computer - 1] == "Rock":
        print("You lose!")
        playAgain()
    elif picks[player - 1] == "Rock" and picks[computer - 1] == "Scissors" or picks[player - 1] == "Paper" and picks[computer - 1] == "Rock" or picks[player - 1] == "Scissors" and picks[computer - 1] == "Paper":
        print("You win!")
        playAgain()
    else:
        sys.exit("Error: Unexpected value.")   

playGame() # execute function