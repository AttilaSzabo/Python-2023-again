import random;
words_for_the_random = ["hegedű","gitár","zongora","harmonika"];
player_letters = [];
one_more_round = ["y","n"]
round = True;


randoms = random.choice(words_for_the_random);
while round:
    player = input("\nPlease give me 1 letter: ");
    player_letters.extend(player)
    for letter in randoms:
        if letter in player_letters:
            print(f" {letter}",end=" ");
        else:
            print(" _ ", end=" ");
    if player == randoms:
        print("You made up a word!");
        while True:
            one_more = input("Would you like another round? Y/N").lower();
            if one_more in one_more_round:
                if one_more == "y":
                    round = True;
                    player_letters = [];
                    randoms = random.choice(words_for_the_random);
                    break;
                elif one_more == "n":
                    round = False;
                    break;
            else:
                print("Y or N please");
        
            