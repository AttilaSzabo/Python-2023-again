# Írj egy Python programot, amely bekér három számot a felhasználótól és kiírja a képernyőre a legkisebb értéket ezek közül!
# Write a Python program that requests three numbers from the user and prints the smallest value of them on the screen!

#Első megoldás
#First solution

def bigger_number():
    numbers1 = [];
    round = 0;
    end_of_round = True;
    while end_of_round:
        if len(numbers1) == 3:
           end_of_round = False;
        else: 
            user = int(input("Please add me 3 numbers: "));
            numbers1.append(user)
            print(f"The users number: {numbers1}")
            print("")
            round +=1;
    the_biggers_number(end_of_round,numbers1)    

def the_biggers_number(kor,szam):
    if kor == False:
        print("The largest number in the list:",max(szam));

bigger_number()

#Második megoldás
#Second solution

def bigger_number():
    numbers2 = [];
    for i in range(3):
        while True:
            try:
                user = int(input("Please enter a number!:"))
                numbers2.append(user);
                break;
            except ValueError:
                print("Invalid input!")
    the_bigger_number(numbers2)


def the_bigger_number(number):
    max_number = max(number)
    print("The largest number in the list: ",max_number)

bigger_number()

