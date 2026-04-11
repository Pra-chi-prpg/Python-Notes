# 1.create a class(2-D vector) and use to create another class representing a 3-D vector 
'''
class twoDvector:
    def __init__(self,i,j):
        self.i = i
        self.j = j
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")

class threeDvector(twoDvector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")

a = twoDvector(1,2)
b= threeDvector(7,2,3)
a.show()
b.show()
'''
# 2.create a cllass "pets" from a class "animal" and further create a class "dog" from "pets" .Add a method "bark" to class "dog"
'''
class animal:
    pass

class pet(animal): 
    pass

class dog(pet):
    @staticmethod
    def bark():
        print("Bow Bow !!")
d = dog()
d.bark()
'''
# 3.create a class "Employee" and add salary and increment properties to it
# write a method 'salaryAfterincrement' method with a @property decorator with a setter which changes the value of increment based on the salary
'''
class Employee:
    salary =234
    increment =20
    @property
    def salaryAfterincrement(self):
        return (self.salary + self.salary *(self.increment/100))
    @salaryAfterincrement.setter
    def salaryAfterincrement(self,salary):
        self.increment = ((salary/self.salary)-1)*100
e= Employee()

print(e.salary , e.increment)
print(e.salaryAfterincrement)
e.salaryAfterincrement = 280.8
print("increment % : ",e.increment)
'''
# 4. writa a class 'Complex' to represent complex numbers, along with overloaded operator '+' and '*' which adds and multiplies them
'''
class Complex:
    def __init__(self ,r ,i):
        self.r = r
        self.i = i
    def __add__(self,c2):
        return Complex(self.r + c2.r, self.i + c2.i)
    
    def __mul__(self,c2):
        real = self.r * c2.r - self.i * c2.i
        imag = self.r * c2.i + self.i * c2.r
        return Complex(real ,imag)
    
    def __str__(self):
        return f"{self.r} + {self.i}i"

c1 = Complex(1,2)
c2 = Complex(3,4)
print(c1 + c2)
print(c1 * c2)
'''
# 5.write a class vector representing a vector of  n dimensions. Overload the + and * operator which calculates the sum and the dot(.) product of them.
''' 
class vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self,other):
        result = vector(self.x + other.x , self.y + other.y , self.z + other.z)
        return result
    def __mul__(self,other):
        result = (self.x * other.x + self.y * other.y + self.z * other.z)
        return result
    
    def __str__(self):
        return f"{self.x} , {self.y} , {self.z} "
    
v1 =vector(1,2,3)
v2 = vector(4,5,6)
v3 = vector(7,8,9)
print(v1 + v2)
print(v1 * v2)

print(v1 + v3)
print(v1 * v3)
'''
# 6. write __str__()method to print the vector as follow:
#  7i + 8j + 10k assume vector for 3 dimension
'''
class vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self,other):
        result = vector(self.x + other.x , self.y + other.y , self.z + other.z)
        return result
    
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k "
    
v1 =vector(1,2,3)
v2 = vector(4,5,6)
v3 = vector(7,8,9)
print(v1 + v2)
print(v1 + v3)
'''
# 7. Override  the __len__()method  on vector of problem 5 to display the dimension of the vector

class vector:
    def __init__(self,l): # or by using(self,*l)
        self.l = l
    def __len__(self):
        return len(self.l)
v1 = vector([1,2,3]) # veector(1,2,3)
print(len(v1))


