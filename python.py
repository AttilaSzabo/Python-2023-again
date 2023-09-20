import random
options = ["kő","papír","olló"];
computer_points = 0;
player_ponts = 0;

while True:    
    player = input("Kérlek válassz a következők közül: Kő, Papír, Olló\n :").lower();
    computer = random.choice(options)
    if player in options:
        if player == computer:
            print("A játék döntetlen \n Újból!");
        elif (
            (player == "kő" and computer == "olló") or
            (player == "papír" and computer == "kő") or
            (player == "olló" and computer == "papír")
        ):
            print("játékos nyert!");
            break;
        else:
            print("A számítóép nyert!");
            break;
    else :
        print("Helytelen opciót adtál meg!")