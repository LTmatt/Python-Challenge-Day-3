print("Welcome to Dragon Island.")
print("Your mission is to escape the dragon")
choice1 = input("You\'re at a crossroad, where do you want to go? Type \"left\" or \"right\"?\n").lower()

if choice1 == "left":
    choice2 = input("You have made the first correct choice, you now see gap in front of you, do you jump or swing across?\n").lower()
    if choice2 == "jump":
        choice3 = input("You now see a red, yellow & green door, which do you choose?\n").lower()
    else:
        print("You died")   
    if choice3 == "red":
        print("You died")
    elif choice3 == "yellow":
        print("You escaped!")
    elif choice3 == "blue":
        print("You find yourself at the start again!")
    else:
        print("You cailed to choose! You died!")    
    
else:
    print("You died")

