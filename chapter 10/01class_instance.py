'''
class Employee():
    language="py" # this is class attribute
    salary=12000
harry = Employee()
harry.name= "Harry Singham" #this is object/instance attribute
print(harry.name,harry.salary,harry.language)
Rohan = Employee()
Rohan.name="Rohan Robinhood"
print(Rohan.name,Rohan.salary,Rohan.language)'''
# here name is the object / instance attribute and 
# #salary and language are class attribute


# instance VS class
'''
class Employee():
    language="py" 
    salary=12000
harry = Employee()
harry.name= "Harry Singham" 
harry.language="JAVA"
print(harry.name,harry.salary,harry.language)
Rohan = Employee()
Rohan.name="Rohan Robinhood"
print(Rohan.name,Rohan.salary,Rohan.language)
'''
# instance attribute takes preference over the class attribute
