f = open("file.txt")
lines=f.readlines()    # type is list
# print(lines,type(lines))

'''
line1 =f.readline()      # type is string
print(line1,type(line1))

line2 =f.readline()
print(line2,type(line2))

line3 =f.readline()
print(line3=="",type(line3))

'''
# if i want to do above work by using "for"  loop
'''for lines in f:
    print(lines)'''

# using while loop
line = f.readline()
while(line != ""):
    print(line)
    line= f.readline()
f.close()

