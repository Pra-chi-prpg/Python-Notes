'''
def avg():
    a = int(input("Enter a number: "))
    b= int(input("Enter another number: "))
    c= int(input("Enter one more number: "))
    average = (a+b+c)/3
    print("The average is:", average)

avg()
avg()
'''
# ARGUMENT
'''
def goodday(name, ending):
    print("Good day ",name)
    print(ending)
    return "okay"
a=goodday("Alice","have a nive day")
print(a)
# goodday("Bob","see you later")
'''
# DEFAULT ARGUMENT
def goodday(name,ending="Thank you!"):
    print("Good Day",name)
    print(ending)
goodday("Alice")
goodday("Bob","See you later")


