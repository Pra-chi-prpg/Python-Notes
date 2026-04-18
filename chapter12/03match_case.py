# match case
'''
def http_status(status):
    match status:
        case 200:
            return "ok"
        case 404:
            return "Not found"
        case 500:
            return "internal server error"
        case  _:
            return "Unknown status"
print(http_status(200))
print(http_status(404))
print(http_status(500))
print(http_status(400))

'''
# dictionary merge
d1={'a':1,'b':2}
d2 = {'c':3,'d':4}
merged =d1|d2
print(merged)
d1 |= d2 
print(d1)