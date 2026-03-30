#1. write a program to find the greatest of four numbers entered by the user
'''
a1 = int(input("Enter the number 1"))
a2 = int(input("Enter the number 2"))
a3 = int(input("Enter the number 3"))
a4 = int(input("Enter the number 4"))

if (a1 > a2 and a1 > a3 and a1 > a4)
    print("Greater number is a1",a1)
elif(a2 > a1 and a2 >a3 and a2 > a4)
    print("Greater number is a2",a2)
elif(a3> a1 and a3>a2 and a3>a4)
    print("Greater number is a3",a3)
elif(a4>a1 and a4>a2 and a4>a3)
    print("Greater number is a4",a4)
'''
# 2.write a program to find out whether a student passed or failed if it requires a total of 40% and atleast 33% in each subject to pass. Assure 3 subjects and take the marks as input from the user.
'''
marks1 = int(input("Enter marks of subject1"))
marks2 = int(input("Enter marks of subject2"))
marks3 = int(input("Enter marks of subject3"))
# check for total percentage
total_percentage = ((marks1 + marks2 + marks3)*100)/300
if (total_percentage >=40 and marks1 >=33 and marks2 >=33 and marks3 >=33)
    print("you have PASSED",total_percentage)
else
    print("you have FAILED",total_percentage)
'''

# 3.A spam comment is defined as a text containing following keywords
# "Make a lot of money", “buy now", "subscribe this", “click this", Write a program to detect these spams.
'''
p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"       
p4 = "click this"
message = input("Enter any comment")
if((p1 in message) or (p2 in message )or (p3 in message) or (p4 in message))
    print("this is A SPAM")
else
    print("this is NOT SPAM")
'''
    

# 4.Write a program to find whether a given username contains less than 10 characters or not.
"""
username = input("Enter username")
if (len(username) < 10)
    print("username is less than 10")
else
    print("greater than 10")
"""
# 5.Wite a program which finds out whether a given name is present in a list or not.
'''
lst =["Harry","Ram","Mohan","Prachi"]
name = input("Enter name")
if (name in lst)
    print("YES")
else
    print("NO")
'''


# 6. Write a program to calculagrade = a st
# dent trom his marks from the following scheme
'''
90-100=>Ex
80-900>A
70-80=>B
60-70=>C
50-60=>D
<50=>F
'''

marks =int(input("Enter marks :"))
if(marks<=100 and marks>=90):
    Grade = "EX"

elif(marks<90 and marks>=80):
    Grade = "A"
elif(marks<80 and marks>=70):
    Grade = "B"
elif(marks<70 and marks>=60):
    Grade = "C"
elif(marks<60 and marks>=50):
    Grade = "D"
elif(marks<50 and marks>=40):
    Grade =  "F"

print(f"your marks is {marks} and grade is {Grade}")

# 7, Wite a program to find out whether a given post is talking about "Harry" or not.
post = input("Enter post: ")
if("Harry".lower() in post.lower()):
    print("YES this post is talking about Harry")
else:
    print("NO")
   
