# 1.Create a Class "Programmer" for storing the information of few programmer work at Microsoft
'''
class Programmer:
    company = "Microsoft"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p1 =Programmer("Rohit",12000,201001)
print(p1.name,p1.salary,p1.pin,p1.company)
p2= Programmer("Pooja",80000,201001)
print(p2.name,p2.salary,p2.pin,p2.company)
'''

# 2. write a class "calculator" capable of finding square,cube,and square root of  a number

# 4. Add a static method in problem 2 , to grrt the user with hello
'''
class calculator:
    def __init__(self,n):
        self.n = n
    
    def square(self):
        print(f"square of {self.n} = {self.n*self.n}")
    
    def cube(self):
        print(f"cube of {self.n} = {self.n*self.n*self.n}")
    
   def sq_root(self):
        print(f"square root of {self.n} = {self.n**(0.5)}")
    
    @staticmethod
    def greet():
        print("HELLO !!!")
a = calculator(4)
a.greet()
a.square()
a.cube()
a.sq_root()
'''
# 3.create a class with class attribute a; create an object from it and set 'a' directly using object.a = 0. Does this change the class attribute
''' No  the class attribute is not change
class demo:
    a=4
obj = demo()
print(obj.a) # prints the class attribute because instance attribute is not present

obj.a = 0 # instance attribute is set
print(obj.a) #  print the instance attribute because instance attribut is present
print(demo.a) #print the class attribute
'''

# 5. Write a class Train which has a method to book a ticket,get status(no of seats) and get fare information of train running under Indian Railway
'''
from random import randint
class Train: 
    def __init__(self,trainNO):
        self.trainNO = trainNO
    def book_ticket(self,fro,to):
        print(f"Ticket is booked in train no: {self.trainNO} from {fro} to {to}")
    
    def get_status(self):
        print(f"Train no :{self.trainNO} is running on Time")
    
    def get_fare_info(self,fro,to):
        print(f"Ticket fare in train no: {self.trainNO} from {fro} to {to} is $ {randint(2222,5555)}")
t1 = Train(12231)
t1.book_ticket("Delhi", "kanpur")
t1.get_status()
t1.get_fare_info("Delhi","Kanpur")
'''
# 6.Can you change the self-parameter inside a class tosomething else(say "harry").Try changing self to "slf" or"harry" and see the effects

from random import randint
class Train: 
    def __init__(slf,trainNO):
        slf.trainNO = trainNO
    def book_ticket(harry,fro,to):
        print(f"Ticket is booked in train no: {harry.trainNO} from {fro} to {to}")
    
    def get_status(slf):
        print(f"Train no :{slf.trainNO} is running on Time")
    
    def get_fare_info(slf,fro,to):
        print(f"Ticket fare in train no: {slf.trainNO} from {fro} to {to} is $ {randint(2222,5555)}")
t1 = Train(12231)
t1.book_ticket("Delhi", "kanpur")
t1.get_status()
t1.get_fare_info("Delhi","Kanpur")

