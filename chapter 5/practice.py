# 1. write a python program to create dictionary of hindi words with value as their english translation.proviide user with an option to look it up!
'''
word = {
    "panni":"water",
    "dost":"friend",
    "khushi":"happiness"
}
user = input("enter the word:")
print(f"meaning of {user} word {word[user]}")
# or
print(word[user])
'''


# 2.write a program to input eight number from user and display all unique numbers (ones)
'''
s = set()
n = (input("enter the number 1 :"))
s.add(n)
n = (input("enter the number 2:"))
s.add(n)
n = (input("enter the number 3:"))
s.add(n)
n = (input("enter the number 4:"))
s.add(n)
n = (input("enter the number 5:"))
s.add(n)
n = (input("enter the number 6:"))
s.add(n)
n = (input("enter the number 7:"))
s.add(n)
n = (input("enter the number 8:"))
s.add(n)
print(s)
'''

# 3.can we have a set with 18(int) and '18'(str) as a value in it?
''' yes we can have 18 as a integer and 18 as a str

s = set()
s.add(18)
s.add('18')
print(s)
'''
# 4.waht will be the length of following set?
'''
s = set()
s.add(20)
s.add(20.0)
s.add('20')
print(s)
print(len(s))
'''

# 5.   s ={} 
# what is the type of s?
''' 
s = {}
print(type(s))
s is a dictionary'''

# 6. create a empty dictionary.Allow 4 friends to enter their favourite language as a value and use key as  their names .Assume that the name are unique
'''
d = {}
lang = input("enter fav lang :")
name =  input("enter name :")
d.update({name:lang})
lang = input("enter fav lang :")
name =  input("enter name :")
d.update({name:lang})
lang = input("enter fav lang :")
name =  input("enter name :")
d.update({name:lang})
lang = input("enter fav lang :")
name =  input("enter name :")
d.update({name:lang})
print(d)
'''

# 7. if the names of 2 friends are same;what will happen to program in problem 6?
'''the value enter later will be updated
enter fav lang :por
enter name :amm
enter fav lang :c++
enter name :amm
enter fav lang :hindi
enter name :langa
enter fav lang :java
enter name :manu
{'amm': 'c++', 'langa': 'hindi', 'manu': 'java'}'''

# so we conclude that value can be same but key must be unique
# 8.if languages of two friends are same;what will happen to program in problem 6?
"""
nothing will happen the value can be same
enter fav lang :java
enter name :omm
enter fav lang :java
enter name :pooja
enter fav lang :c++
enter name :riya
enter fav lang :python 
enter name :aman
{'omm': 'java', 'pooja': 'java', 'riya': 'c++', 'aman': 'python '}
"""

# 9.can you change the value inside a list which is contained in set S?
s = {8,7,12,"Harry",{1,2}}
# ❌ No, you cannot change the value inside a list contained in a set, because you cannot add a list to a set at all — lists are unhashable.