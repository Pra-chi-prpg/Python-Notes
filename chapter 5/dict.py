
d = {} #empty dictionary
marks = {
    "Rohan": 85,
    "Aisha": 92,
    "Kiran": 78,
}

# print(marks["Aisha"])
# print(marks, type(marks))
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({
    "Rohan" : 90,
    "Prachi": 100
              })
print(marks)
# print(marks.get("Viran"))   #prints None
# print(marks["Viran"])  #raise the key error
marks.pop("Kiran")  #removes the key-value pair
print(marks)
new_marks = marks.copy()
print(new_marks)
print(marks.popitem())  #removes the last key-value pair
print(marks)
marks.clear()  #removes all key-value pairs
print(marks)  # prints an empty dictionary
new_dict = marks.fromkeys(["Rohan", "Aisha"], 0)
print(new_dict)  # creates a new dictionary with specified keys and a default value
