import random
num=random.randint(1,100)
while True:
    try:

        userinput=int(input("\nEnter the number you want: "))

        if userinput>num:
            print("The number you entered is too greaterthan generated one.")
        elif userinput<num:
            print("The number you entered is too lessthan generated one.")
        else:
            print("Wow, you won the game.")
    except ValueError:
        print("Invalid input. try again.")
    terminate=input("You want to continue? ").strip().lower()
    if terminate=="no":
        print("Thank you for playing this game. Nice day.\n")
        break
    
