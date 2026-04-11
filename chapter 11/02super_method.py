
class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a=1

class programmer(Employee):
    def __init__(self): 
        print("Constructor of programmer")
    b=2

class Manager(programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
    c= 3
# o = Employee()
# print(o.a) # print "a" attribute but on "b" and "c" it show an error that it has  no attribute in Employee class
# o = programmer()
# print(o.a,o.b) # on "c" it show error as it do not have "c" attribute on programmer
o = Manager()
print(o.a, o.b, o.c)