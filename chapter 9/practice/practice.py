
# 1. write a program to read the text from a given file 'poems.txt' and find out whether it contain the word "twinkle"
'''
f= open("poems.txt")
content =f.read()
if ("twinkle" in content):
    print("yes it is present")
else:
    print("not present")
f.close()
'''
# 2.The game() function in a program lets a user play a game and read the score as a integer.you need to read a file 'HI-score.txt' which is either blank or contains the previous HI-score.
# You need to write a program to update the HI-score whenever the game( )function breaks the Hi-score
'''
import random
def game():
    print("Game is  starting")
    score =random.randint(1,50)
    # fetch the hiscore
    with open("hiscore.txt")as f:
        hiscore = f.read()
        if (hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print("your score is: ",score)
    if (score>hiscore ):
        # write this hiscore in file
        with open("hiscore.txt","w") as f:
            f.write(str(score))


    return score

game()
'''
# 3.write a program to generate a multiplication tables from 2 to 20 and write it to different files.place in a folder for a 13 - year old
'''
def generateTable(n):
    table=""
    for i in range(1,11):
        table += f"{n} X {i} ={n*i}\n"
    with open(f"tables/ table_{n}.txt","w") as f:
        f.write(table)

for i in range(2,21):
    generateTable(i)
'''
# 4. A file contain a word "Donkey" multiple times. You need to write a program  which replace this word with ##### by updating the same file
'''
word ="Donkey"
with open("poems.txt","r")as f:
    content = f.read()
    new_content = content.replace(word,"#####")
with open("poems.txt","w") as f:
   f.write(new_content)
'''
# 5. Repeat program 4 for a list of such word to be censored  
'''
words =["Donkey","bad","ganda"]
with open("poems.txt","r")as f:
    content = f.read()
for word in words:
    content = content.replace(word,"#"*len(word))
with open("poems.txt","w") as f:
   f.write(content)
'''
# 6.write a program to mini a log file and find out whether it contains'python'
'''
with open("log.txt") as f:
    content= f.read()
    if ("python" in content.lower()):
        print("yes it is present")
    else:
        print("not present")
'''
# 7.write a program to find out the line number where the python is present from ques 6
'''
with open("log.txt") as f:
    lines = f.readlines()
lineno=1
for line in lines:
    if ("python" in line):
        print(f"yes it is present in line: {lineno}")
        break
    lineno += 1
else:
        print("not present")
     '''  
# 8. write a program to make a copy of a text file "this.txt"
'''
with open("this.txt")as f:
    content = f.read()
with open("this_copy.txt","w") as f:
    f.write(content)
'''
# 9.write a program to find out whether a file is identical & matches the content of another file
'''
with open("poems.txt")as f:
    content1 = f.read()
with open("this_copy.txt") as f:
    content2 = f.read()
if (content1 == content2):
    print("yes file is identical")
else:
    print("file is not identical")
'''
# 10.write a program to wipe out the content of file using python
'''
with open("this_copy.txt","w")as f:
    f.write("")
'''

# 11. write a python program to rename a file to "renamed_by_python.txt"
with open("old.txt","r")as f:
    content = f.read()
with open("renamed_by_python.txt","w")as f:
    f.write(content)
