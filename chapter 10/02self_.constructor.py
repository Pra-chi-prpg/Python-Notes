# STATIC METHOD and Self Parameter

class employee:
    salary = 12345
    lang = "PyTHON"

    def __init__(self,name,salary,lang):   # dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.lang = lang
        print("I am creating an object")

    def getInfo(self,naam):
        print(f"The language is:{self.lang}__ {naam} The salary is {self.salary}")

    @staticmethod
    def greet():
        print("good Morning")
harry = employee("Harry",12000,"RUBY")
# harry.lang="java"
harry.getInfo("paroo")
# employee.getInfo(harry)
harry.greet()
print(harry.name,harry.salary,harry.lang)
# __init__ / CONSTRUCTOR

         