import random
options = ["rock","paper","scissors"];

def run_game (x):
    while True:
        player = input("Please choose from: Rock, Paper, Scissors: ").lower();
        computer = random.choice(x);
        if player in x:
            winner = game_evaluation (player, computer);
            print (winner);
            if winner != "The game is a draw!":
                break;
        else:
            print("Bad choice!")

def game_evaluation (player, computer):
    if player == computer:
        return "The game is a draw!"
    elif (
        (player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock")  or
        (player == "scissors" and computer == "paper")
    ):
        return "The player Won!"
    else:
        return "The computer won!"


    
run_game(options)

