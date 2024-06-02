import sys
import random
from enum import Enum

game_count = 0

def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    picks = ["Rock", "Paper", "Scissors"]
    playerchoice = input("Enter...\n1 for Rock,\n2 for Paper,\n3 for Scissors: \n\n")
    
    player = int(playerchoice)
    computerchoice = random.choice("123")
    computer = int(computerchoice)
    
    if playerchoice not in ["1", "2", "3"]:
        print("You must enter a value between 1-3.")
        return play_rps()
    else:
        print("")
        print("You chose " + str(RPS(player)).replace('RPS.','') + ".")
        print("Python chosen " + str(RPS(computer)).replace('RPS.','') + ".")
        print("") 
    
    def decide_winner(player, computer): 
        if picks[player - 1] == "Rock" and picks[computer - 1] == "Rock" or picks[player - 1] == "Paper" and picks[computer - 1] == "Paper" or picks[player - 1] == "Scissors" and picks[computer - 1] == "Scissors":
            print("No one wins!")
        elif picks[player - 1] == "Rock" and picks[computer - 1] == "Paper" or picks[player - 1] == "Paper" and picks[computer - 1] == "Scissors" or picks[player - 1] == "Scissors" and picks[computer - 1] == "Rock":
            print("You lose!")
        elif picks[player - 1] == "Rock" and picks[computer - 1] == "Scissors" or picks[player - 1] == "Paper" and picks[computer - 1] == "Rock" or picks[player - 1] == "Scissors" and picks[computer - 1] == "Paper":
            print("You win!")
        else:
            sys.exit("Error: Unexpected value.")   
    
    game_result = decide_winner(player, computer)
    
    global game_count
    game_count += 1
    
    print("\nGame count: " + str(game_count))
    print("Play again?")
    while True:
        playagain = input("Y for Yes or \nQ to Quit \n")
        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break
    
    if playagain.lower() == "y":
        return play_rps()
    else:
        print("\n🎉🎉")
        print("Thank you for playing!\n")
        sys.exit("Bye!")

play_rps()