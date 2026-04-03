'''
f=open("file.txt")
print(f.read())
f.close()
'''
# # the same can be written using "with statement"
with open("file.txt")as f:
    print(f.read())
# here we don't need to close the file as it is automatically closed after the execution of the block
# this is the advantage of using "with statement"

str = "prachi"
with open("myfile.txt","a")as f:
    f.write(str)    