#1. write a program to store seven fruit in list entered by the user.
"""
fruits =[]
f2 = int(input("enter the fruit: "))
fruits.append(f2)
f3 = int(input("enter the fruit: "))
fruits.append(f3)
f4 = int(input("enter the fruit: "))
fruits.append(f4)
f5 = int(input("enter the fruit: "))
fruits.append(f5)
f6 = int(input("enter the fruit: "))
fruits.append(f6)
f7 = int(input("enter the fruit: "))
fruits.append(f7)
print("list of fruits is:",fruits)
"""
# 2.write a  program to accept marks of 6 students and display them in sorted manner
"""
marks =[]
f2 = int(input("enter the marks: "))
marks.append(f2)
f3 = int(input("enter the marks: "))
marks.append(f3)
f4 = int(input("enter the marks: "))
marks.append(f4)
f5 = int(input("enter the marks: "))
marks.append(f5)
f6 = int(input("enter the marks: "))
marks.append(f6)
# marks.sort()
# print(marks)
# or
c = sorted(marks)
print(c)"""

"""marks.sort()-------Use .sort() when you want to modify the original list.
c = sorted(marks)----Use sorted() when you want a new sorted list without changing the original."""


# 3. checked that tuple type cannot be changed in python 
'''
a = (1,3,"hello")
a[2]="world"
print(a)
'''

# 4.write a program to sum list with 4 numbers
lst =[1,3,5,7]
print(sum(lst))

# 5. write a program to count the number of zeros in the following tuple
# a = (7,0,8,0,0,9)
# t = a.count(0)
# print(t)