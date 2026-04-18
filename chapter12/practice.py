# 1.write a program to open three files 1.txt ,2.txt ,3.txt if any of this file is not present, amessage without existing the program must be printed prompting the same
'''
try:
    with open("1.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open("2.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)

try:
    with open("3.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)
print("end of problem")
'''
#2. write a program yto print third,fifth and seventh element from a list using enumerate function
'''
l =[1,2,3,4,5,6,7,8]
for i,item in enumerate(l):
    if (i == 2 or i == 4 or i == 6):
        print(f"{i} item at the given position {item}")
else:
    print("not found")
'''
# 3.write a list comprehension to print a list which contain multiplication table of user enter a number
'''
n =int(input("Enter a number : "))
table = [n*i for i in range(1,11)]

print(table)
'''
# 4.write a program to display a/b where a and b are integers .If b=0, display infinite by handling the 'ZeroDivisionError'
'''
try:
    a=int(input("Enter a number a : "))
    b=int(input("Enter a number b : "))
    print(a/b)
except ZeroDivisionError :
    print( "Infinite")
'''
# 5.store the multiplication tables generated in problem 3 in a file named table.txt
n =int(input("Enter a number : "))
table = [n*i for i in range(1,11)]
with open("table.txt","a") as f:
    f.write(f"Table of {n} = {str(table)}\n")