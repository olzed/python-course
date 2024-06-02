# Guess number
# uses args, similar to RPS

import sys
import random

def guess_number(name='Player'):
    gameCount = 0
    player_wins = 0
    
    def playGame():
        nonlocal name
        nonlocal player_wins
        
        numChoice = input(f"\n{name}, guess which number I am thinking of... 1, 2, or 3.\n")
        randNum = random.choice("123")
        
        if numChoice not in["1", "2", "3"]:
            print(f"{name} please enter a value of 1, 2, or 3.")
            return playGame()
        else:
            print(f"\n\nYou chose {numChoice}.")
            print(f"The number was {randNum}.")
            
        def gameWinner():
            nonlocal player_wins
            if numChoice == randNum:
                player_wins += 1
                return f"Congratulations {name}, you win!"
            else: 
                return f"Unfortunately, {name}, you didn't win on this occasion."
                
        gameResult = gameWinner()
        
        nonlocal gameCount
        gameCount += 1
    
        
        print(f"\nGame count: {str(gameCount)}")
        print(f"\n{name} wins: {str(player_wins)}")
        print(f"\nYour winning percentage: {player_wins / gameCount * 100:.2f}%\n")
        print(f"Play again, {name}?")
        while True:
            rematch = input("Y for Yes \nQ to Quit ")
            if rematch.lower() not in ["y", "q"]:
                continue
            else:
                break
            
        if rematch.lower() == "y":
            return playGame()
        else:
            print("Thank you for playing!\n")
            sys.exit(f"Bye, {name}!")
            
    return playGame()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()

    guessNum = guess_number(args.name)
    guessNum()
        
        
        