from random import choice

capital = "Lorem"

bird = "ipsum"

flower = "dolor"

song = "sit amet"

def randomfunfact():
    funfacts = [
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris tincidunt mi et malesuada lacinia. Etiam.",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam velit massa, tristique eget tristique at.",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sed auctor lorem, at finibus metus."
    ]
    
    index = choice("012")
    
    print(funfacts[int(index)])
    
# function only called if this is main file
if __name__ == "__main__":
    randomfunfact()