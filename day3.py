print("Welcome To treasure Island \n Your mission is to find the treasure")
first_input = input("Choose left or right for your future ")
if(first_input == "left"):
    second_input = input("What do you want to do swim or wait ")
    if(second_input == "wait"):
        third_input = input("Which Door do you prefer in foll. colors 'Red','Blue', 'Yellow' ")
        if(third_input == "red"):
            print("You are burned by fire")
        elif(third_input == "blue"):
            print("You are eaten by Beasts")
        elif(third_input == "yellow"):
            print("You Win")
        else:
            print("Game just over")
    else:
        print("You are attacked by trout")
else:
    print("Fall into a hole")
