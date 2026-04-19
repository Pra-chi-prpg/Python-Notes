# 1. create two virtual environments,install few  packkages in the first one. How do you create a similar environment int he second one

#  2. write a program to input name ,marks and phone number of a student and format it using the format function like below:
# "The name of the student is Harry ,his marks are 72 and phone number is 99998888"
'''
name = input("Enter Name :")
marks =int(input("Enter marks: "))
phone_no = int(input("Enter phone no.: "))
data =("The name of the student is {} ,his marks are {} and phone number is {}").format(name,marks,phone_no)
print(data)
'''
# 3. A list contain the multiplication table of 7 .Write a program to convert it to vertical string of the same number.
'''
table = [str(7*i )for i in range(1,11)]
s ="\n".join(table)
print(s)
print(type(s))
'''
# 4. write a program to filter a list of number divisible by 5
'''
def div_5(n):
    return n%5 == 0 # we can also do this problem by using this
# OR
def div_5(n):
    if (n%5 == 0):
        return True
    else:
        return False

a=[12,35,67,88,96,100,25]
f =list(filter(div_5,a))
print(f)

'''
#  5.write a program to find the maximum of the numbers in alist using the reduce function
'''
from functools import reduce
l=[12,35,11,111,67,88,96,100,25]
def greater(a,b):
    if(a>b):
        return a
    return b
val =reduce(greater,l)
print(val)
'''
# 6.  Run pip freeze for the system interpreter. Take the contents and create a simple virtualenv
'''
pip freeze > requirements.txt
virtualenv henv
\.henv\Script\activate
pip install -r requirements.txt
'''
# 7. Explore the Flask module and create a webserver using Flask and Python


