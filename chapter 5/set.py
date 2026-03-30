# e = set()      #empty set don't use s={} as it creates an empty dictionary
# print(type(e))      # prints <class 'set'>
# s = {1,3,4,5,2,34,5,5,5,5,"harry",2}
# s.add(6)
# print(s)
# s.clear()
# print(s)
# new_set =s.copy()
# print(new_set)
# s1 = {1,2,3,4}
# s2 = {3,4,5,6}
# print(s1.difference(s2))
# print(s1.intersection(s2))
# print(s1.union(s2))
# s.remove("harry")
# print(s)  
# print(s.pop())
# print(s) 
s ={1,2,3,4,5,6,7,8} 
t = {1,2,13,4,5}
print(t.discard(13))  # removes 30 if it exists, does nothing if it doesn't
print(t)
print(len(t))
# print(t.isdisjoint(s))  # checks if two sets have no elements in common
print(t.issubset(s))  # checks if t is a subset of s
print(s.issuperset(t))  # checks if t is a superset of s
# print(s - t)
# print(s | t)  # union of s and t    
# print(s & t)  # intersection of s and t
# print(s ^ t)  # symmetric difference of s and t
# s.update({9,10,11})
# print(s)
