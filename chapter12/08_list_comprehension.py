l = [1,2,4,5]
'''
square_list = []
for item in l:
    square_list.append(item*item)
print(square_list)
'''
# by using list comprehension

sq = [item*item for item in l]
print(sq)