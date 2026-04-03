"""
sanke - water - gun
1 for snake
-1 for water
0 for gun

"""
import random

computer = random.choice((1, -1, 0))
youstr = input("Enter your choice (s/w/g): ")

youDict = {"s":1, "w":-1, "g":0}

if youstr not in youDict:
    print("Invalid input! Please enter s, w or g.")
else:
    you = youDict[youstr]

    reverseDict = {1:"snake", -1:"water", 0:"gun"}
    print(f"computer chose: {reverseDict[computer]}\n your choice: {reverseDict[you]}")

    if computer == you:
        print("Draw")
    else:
        if (computer == -1 and you == 1):
            print("WIN")
        elif (computer == -1 and you == 0):
            print("LOSE")
        elif (computer == 1 and you == 0):
            print("WIN")
        elif (computer == 1 and you == -1):
            print("LOSE")   
        elif (computer == 0 and you == 1):
            print("LOSE")
        elif (computer == 0 and you == -1):
            print("WIN")   
            
'''
logic that can be used from above

-1 and 2 =>lose
1 and -2 =>win

elif (computer - you) == -1 or (computer - you == 2):
    print("YOU LOSE")
else:
    print("WINNER")'''
