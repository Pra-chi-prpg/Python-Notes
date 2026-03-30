# n= int(input("enter a number : "))
# fact = 1
# for i  in range(1,n+1):
#     fact = fact*i
# print("factorial of",n,"is",fact)


n=int(input("enter a number : "))
def factorial(n):
    if n==0 or n==1:
        return 1
    return n * factorial(n-1)
print("factorial of",n,"is",factorial(n))