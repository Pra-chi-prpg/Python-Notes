'''
try:
    a=int(input("Hey, Enter a number : "))
    print(a)
except ValueError as v:
    print("value error")
    print(v)
except Exception as e:
    print(e)

print("Thank You")
'''
# RAISE An error
'''
a=int(input("enter a number : "))
b= int(input("enter second number : "))
if(b == 0):
    raise ZeroDivisionError ("hey you can not divide any number with zero")
else:
    print(f"the division a/b is: {a/b} ")
'''
# TRY _else 
'''
try:
    a=int(input("Enter a number : "))
    print(a)
except Exception as e:
    print(e)
else:
    print("safe")
'''

# Finally
def main():
    try:
        a=int(input("Enter a number : "))
        print(a)
        return
    except Exception as e:
        print(e)
        return
    finally:
        print("hey i am inside finally")
main()