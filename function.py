import random
options = ["rock","paper","scissors"];

def run_game (x):
    while True:
        player_score = 0;
        computer_score = 0;
        player = input("Please choose from: Rock, Paper, Scissors: ").lower();
        computer = random.choice(x);
        if player in x:
            winner = game_evaluation (player, computer);
            print (winner);
            if winner != "The game is a draw!":
                score (winner,player_score,computer_score)
                winner_score (player_score,computer_score)
            if player_score == "3" or computer_score == "3":
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

def score (w,p,c):
    if w == "The player Won!":
        p+=1;
    else:
        c+=1;

def winner_score (p_s,c_s):
    if p_s == "3":
        print("Players its winner")
    elif c_s == "3":
        print("Computer its winner")

run_game(options)

