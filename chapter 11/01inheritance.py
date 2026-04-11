# TYPE OF INHERITANCE
# Single Inheritance
'''class employee:
    company="ITC"
    def show(self):
        print(f"The name is{self.name} and the salary is {self.salary}")
        
# class programmer:
#     company="ITC Infotech"
#     def show(self):
#         print(f"The name is{self.name} and the salary is {self.salary}")
#     def show_lang(self):
#         print(f"The name is {self.name} and he is good with {self.lang} language")

# this is done by inheritance 
class programmer(employee):
     company = "ITC INFOTECH"
     def show_lang(self):
        print(f"The name is {self.name} and he is good with {self.lang} language")


a = employee()
b= programmer()
print(a.company , b.company)
'''


# Multiple inheritance
'''
class Employee:
    company = "ITC"
    name = "COOCUU"
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")
        
class coder:
    language = "python"
    def printLang(self):
        print(f"out of all  the language here is your language {self.language}")

class programmer(Employee,coder):
     company = "INFOTECH"
     def show_lang(self):
        print(f"The name is {self.name} and he is good with {self.language} language on  {self.company}")

a= Employee()
b = programmer()
a.show()
print(a.company,b.company)
b.show()
b.printLang()
b.show_lang()
'''

# Multilevel inheritance
 
class Employee:
    a=1

class programmer(Employee):
    b=2

class Manager(programmer):
    c= 3
o = Employee()
print(o.a) # print "a" attribute but on "b" and "c" it show an error that it has  no attribute in Employee class
o = programmer()
print(o.a,o.b) # on "c" it show error as it do not have "c" attribute on programmer
o = Manager()
print(o.a, o.b, o.c)