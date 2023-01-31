from random import randint

moves = ['rock', 'paper', 'scissors']

while True:

    computer = moves[randint(0,2)]

    player = input('rock, paper or scissors (or end the game?)').lower()


    if player == 'end the game':
        print("The game has been Ended!")
        break


    elif player == computer:
        print("Game Tied!")


    elif player == "rock":
        if computer == "paper":
            print("You are a Looser !!!", computer, " beats ", player)
        else:
            print("You are a Winner !!!" ,player, " beats " ,computer)


    elif player == "paper":
        if computer == "scissors":
           print("You are a Looser !!!", computer, " beats ", player)
        else:
            print("You are a Winner !!!" ,player, " beats " ,computer)


    elif player == "scissors":
        if computer == "stone":
            print("You are a Looser !!!", computer, " beats ", player)
        else:
            print("You are a Winner !!!" ,player, " beats " ,computer)


    else:
        print("Please Enter the correct spelling!")
