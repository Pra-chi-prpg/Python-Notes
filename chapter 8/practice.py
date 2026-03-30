# 1.write a program using functions to find greatest og three number.
'''
a= 1
b =23
c=3
def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
print("greatest number is",greatest(a,b,c))
'''

# 2.write  a program using function to convert celsius to Fahrenheit.
'''
celcuis = int(input("enter temperature in celsius: "))
def convert(celcuis):
    farenheit = (celcuis* 9/5)+32
    return farenheit
print("celcius to farenheit is:",convert(celcuis))
a= convert(celcuis)
print(f"rounded off value of celcius is: {round(a,0)}")
'''

'''
f = int(input("enter temperature in f: "))
def convert(f):
    return 5*(f-32)/9
c=convert(f)
print(f"{round(c,7)}")
'''



# 3.how do you prevent a python print() function to print a new line at the end
'''print("a")
print("b")
print("c",end="")
print("d",end= "")
'''
# 4.wite a recursive function to calculate the sum of first n natural numbers.
'''
n= int(input("enter a number: "))
def sum(n):
    if n == 0:
        return 0 
    elif n == 1:
        return 1
    return sum(n-1) + n
print("sum of first n natural numbers is:",sum(n))
'''

# 5. write a python function to print  first n lines of the following pattern:
'''
***
**
* n=3
def pattern(n):
    if n==0:
        return
    print("*"*n)
    pattern(n-1)
pattern(3)
'''

# 6.write a python function which can convert inches to cms
'''
i = int(input("enter inches: "))
def i_to_cm(i):
    cm = i * 2.54
    return cm
print("inches to cm is:",i_to_cm(i))
 
'''

# 7. write a python function to remove a given word from a list and strip it at the same time
'''
l = ["Rohan","harry","Sohan","an"]
def rem (l,word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n
    
print(rem(l,"an"))
'''

# 8. write apython function to print multiplication table of given number
def multiply(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")
multiply(12)


