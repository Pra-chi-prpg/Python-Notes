from functools import reduce
# Map example
l =[1,2,3,4,5]
square = lambda x:x*x
sqList =map(square,l)
print(list(sqList))

# filter example
def even(n):
    if(n%2 == 0):
        return True
    return False
onlyEven=list(filter(even,l))
print(onlyEven)

# Reduce Example
def sum(a,b):
    return a+b
print(reduce(sum ,l))

mul = lambda x,y:x*y
print(reduce(mul,l))