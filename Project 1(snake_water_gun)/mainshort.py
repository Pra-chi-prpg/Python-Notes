import random
computer = random.choice([-1,0,1])

youstr = input("Enter your choice: ")
youDict={"s":1,"w":-1,"g":0}
reverseDict={1:"snake",-1:"water",0:"gun"}
you= youDict[youstr]

print(f"computer chose : {reverseDict[computer]}\n you chose :{reverseDict[you]}")
if (computer == you):
    print("DRAW")
elif (computer - you) == -1 or (computer - you == 2):
    print("YOU LOSE")
else:
    print("WINNER") 
'''else:
    if(computer == -1 and you == 1):(computer - you) = -2
        print("YOU WIN")
    elif(computer == -1 and you == 0):(computer - you) = -1
        print("LOSE")
    elif(computer == 1 and you == -1):(computer - you) = 2
        print("LOSE")
    elif(computer == 1 and you == 0):(computer - you) = 1
        print("YOU WIN")
    elif(computer == 0 and you == 1):(computer - you) = -1
        print("LOSE")
    elif(computer == 0 and you == -1):(computer - you) = 1
        print("YOU WIN")

    else:
        print("something went wrong")'''

'''
logic that can be used from above

-1 and 2 =>lose
1 and -2 =>win
'''


