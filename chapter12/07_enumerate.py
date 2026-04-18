l = [34,45,56,67]
'''
index=0
for item in l:
    print(f"the item number {index} is {item}")
    index= index+1
'''
# this can be done by enumerate
for index,item in enumerate(l):
    print(f"the item number {index} is {item}")
  