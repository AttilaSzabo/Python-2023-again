
def enter_password():
    password = "123"
    correct_input = True;
    right_try = 0;
    while correct_input:
        user = input("Please enter your password: ");
        if user == password:
            print("The password is correct!");
            choice_options()
            print("")
            correct_input = False
        elif user != password:
            print("The password is incorrect!");
            print("")
            right_try +=1;
            if right_try == 3:
                print("The card has been reserved, please report to the bank branch!");
                correct_input = False;

def choice_options():
    account_balance = 1000.50;
    options = {
        "Check your balance":1,
        "Cash withdrawal":2,
        "account_balance": 3
        }
    print("")
    print(f"Choose from the following options:")
    print("")
    for x, y in options.items():
        print(f"{x}, button {y}")
    while True:
        try:
            user = int(input("Enter number: "));
            if user > 3:
                print("Please enter correctly value!")
            else:
                print("Igen helyes a bemenet!")
                break;
        except ValueError:
            print("")
            print("Please enter correctly value!")


enter_password()
