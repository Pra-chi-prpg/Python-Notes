# # multiple if statement
a = int(input("Enter your age:"))

# if statement no. 1
if (a%2 == 0):
    print("Even")
# Ends of if statement no.1 


# if statement no. 2
# if elif else ladder
if (a>=18):
    print("you are above the age of consent")
elif(a<0):
    print("you are entering Invalid age")
elif(a==0):
    print("you are entering 0 which is not a valid age")
else:
    print("you are below the age of consent")
# Ends of if statement number 2

print("program ends here!!!")

