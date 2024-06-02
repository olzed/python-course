import sys
import random

def arcade(name='Player'):
    welcome_back = False
    
    while True:
        if welcome_back == True:
            print(f"\n{name}, welcome back to the Arcade menu.")
        
        gameChoice = input("Please choose a game:\n1 = Rock Paper Scissors\n2 = Guess My Number\nX to exit the menu ")
        
        if gameChoice not in ["1", "2", "x"]:
            print(f"\n{name}, please enter 1, 2, or X.")
            return arcade(name)
        
        welcome_back = True
        
        if gameChoice == "1":
            from rps import rps
            gameRPS = rps(name)
            gameRPS()
        elif gameChoice == "2":
            from guess_number import guess_number
            guessNum = guess_number(name)
            guessNum()
        else:
            print("\nSee you next time!\n")
            sys.exit(f"Bye {name}!")
            
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
    
    arcade(args.name)