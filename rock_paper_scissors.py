import random 

def rock_paper_scissors():
    options = ["rock","paper","scissors"]
    round = True;
    player_score = 0;
    computer_score = 0;
    while round:
        player = input("Please choose: Rock, Paper, Scissors\n: ").lower();
        computer = random.choice(options);
        if player in options:
            player_score, computer_score = score(player,computer,player_score,computer_score)
            round = ultimate_winner(player_score,computer_score,round)
        else:
            print("please enter a correct value!")


def score(player,computer,player_score,computer_score):
    if player == computer:
        print("The game is a draw!");
    elif (
        (player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock")  or
        (player == "scissors" and computer == "paper")
    ):
        player_score +=1;
        print(f"Player won! \n The player score is: {player_score} \n The computer score is: {computer_score}");
        
    else:
        computer_score +=1;
        print(f"Computer won! \n The player score is: {player_score} \n The computer score is: {computer_score}");
    return player_score, computer_score
    
def ultimate_winner(j_pont,sz_pont,round):
    if j_pont == 3:
        print("The player won the round!");
        return False;
    elif sz_pont == 3:
        print("The computer won the round!");
        return False;
    else:
        return True;


rock_paper_scissors()