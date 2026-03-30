# 1. write a program to print multiplication of table by using for loop
'''
n= int(input("enter a number: "))
for  i in range(1,11):
    print(f"{n} X {i} = {n*i}")
'''

# 2. write a program to greet all the person names stored in a list 'l' and which starts with S.
'''l = ["Harry","Sohan","Sachin","Rahul","Sonam"]
for name in l:
    if name.startswith("S"):
    # if name.endswith("m"):
        print(name)'''

# 3. attempt proble 1 by using while loop
'''n = int(input("enter a number: "))
i=1
while(i<=10):
    print(f"{n} X {i} = {n*i}") 
    i = i + 1'''

#  4.  write a program to find whether a given number is prime or not

'''n= int(input("Enter a number : "))
if n>1:
    for i in range(2,n):
        if n % i == 0:
            print("not prime")
            break
    else:
        print("prime")
else:
    print("not a prime")        
'''
#  5. write aprogram to find the sum of first n natural numbers using while loop.
'''n= int(input("enter a number : "))
i=1
sum = 0
while(i<=n):
    sum = sum + i
    i= i+1
print("sum of first",n,"number : ",sum)
'''
# 6.write a program to calculate the factorial of anumber using for loop
'''n=int(input("Enter a number : "))
fact = 1
for i in range(1,n+1):
    fact = fact*i
    print(fact) 
print(f"the factorail of {n} is {fact}")'''


#  7.write a program to pprint the star pattern:
"""
     *
    ***
   ***** for n = 3

n = int(input("Enter a number : "))
for i in range(1,n+1):
    print(" "*(n-i), end ="" )
    print("*"*(2*i-1),end = "")
    print("")"""

# 8.write a priogram to printthe star pattern
'''
    *
    **
    ***  for n = 3

n= int(input("Enter a number : ")) 
for i in range(1,n+1):
    print("*"*i, end="")
    print("")
'''
#  9. write aprogram to print the following star pattern
'''
***
* *
***
n = int(input("Enter a number : "))
for i  in range(1,n+1):
    if i == 1 or i == n:
        print("*"*n, end ="")
    else:
        print("*",end ="")
        print(" "*(n-2),end = "")
        print("*",end ="")
    print("")
'''
#  10. write a program to print multiplication table of n using for loops in reversed order
n= int(input("enter a number: "))
for i in range(1,11):
    print(f"{n} X {11-i} = {n*(11-i)}")





