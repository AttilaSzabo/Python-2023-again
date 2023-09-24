
def enter_password():
    password = "123";
    correct_input = True;
    right_try = 0;
    while correct_input:
        user = input("Please enter your password: ");
        if user == password:
            print("The password is correct!");
            choice_options();
            print("");
            correct_input = False;
        elif user != password:
            print("The password is incorrect!");
            print("")
            right_try +=1;
            if right_try == 3:
                print("The card has been reserved, please report to the bank branch!");
                correct_input = False;


def choice_options():
    account_balance = 1000.00;
    options = {
        "Cash withdrawal":1,
        "Check your balance":2
        }
    print("");
    print(f"Choose from the following options:")
    print("");
    for x, y in options.items():
        print(f"{x}, button {y}")
    while True:
        try:
            user = int(input("Enter number: "));
            if user > 3:
                print("Please enter correctly value!");
            else:
                selected_options(user,account_balance);
                break;
        except ValueError:
            print("");
            print("Please enter correctly value!");


def selected_options(user,balance):
    if user == 1:
        money_withdrawal(balance);
    elif user == 2:
        print(f"Your account balance: {balance:.2f} €");


def money_withdrawal(money):
    correct_input = True;
    while correct_input:
        try:
            user = int(input("Enter the amount: "));
            if user > money:
                print("You don't have that much money in your account!");
            elif user % 5 != 0:
                print("You cannot withdraw less than 5 euros!");
            else:
                result = f"{money - user:.2f}"
                print(f"Amount withdrawn: {user}");
                print(f"You have {result} € amounts left on your account!");
                correct_input = False;
        except ValueError:
            print("Please enter correctly value!");

enter_password()
