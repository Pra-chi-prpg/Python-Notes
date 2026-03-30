#1. to display a user entered name followed by good afternoon using input{}function
name= input("Enter your name:")
print("good afternoon"+name+"") #concatinate
print(f"good morning {name}") # f string is used


#2. fill the template with name and date
letter='''Dear <|Name|>,
You are selected!
<|Date|>'''
print(letter.replace("<|Name|>","Prachi").replace("<|Date|>","24 sep"))



# 3.writ a program to detect double space in string
name ="my name is prachi   I am a girl"
print(name.find("   "))

# 4.replace the double space from problem 3 with single space
name ="my name is prachi   I am a girl"
print(name.replace("   "," "))

# 5.write a program to format the string using escape string sequence character
letter="Dear Prachi,\n\tThis Python course is nice.\nThanks!"
print(letter)



