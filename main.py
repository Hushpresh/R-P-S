# (R, P and S) Rockun, Paper and Scissors Play
from random import randint 

#The game
steps = ["r", "p", "s"]
while True:
    computer = steps[randint(0,2)]
    person = input("r, p or s? (or win)").lower()
    if person == "win":
        print("you just won the game.")
        break
    elif person == computer:
        print("Tieeeeeeeee")
    elif person == "r":
        if computer == "p":
            print("You lose", computer, "Computer beats Person", person)
        else:
            print("You win!!", person, "Person beats Computer", computer)
    elif person == "p":
        if computer == "s":
            print("You lose!", computer, "Computer beats Person", person)
        else:
            print("You win!!!", person, "Person beats Computer", computer)   
    elif person == "s":
        if computer == "r":
            print("You lose", computer, "Computer beats Person", person)
        else:
            print("You win!!", person, "Person beats Computer", computer)   
    else:
        print("An error, input again")                   