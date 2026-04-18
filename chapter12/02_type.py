from typing import List ,Union ,Tuple,Dict
'''
# variable type hint
n: int = 5
name : str = "harry"
age : int =25
print(n,name,"age is: ",age)

# function type hints
def sum(a:int ,b:int ) -> int:
    return a+b
print(sum(4,5))
'''

number :List[int] = [1,2,3,45,5]
print(number ,type(number))

person: Tuple[str,int] =("alice",12,30)
print(person , type(person))

score :Dict[str,int] ={"harry":1,"Bob":2}
print(score,type(score))

identifier :Union[int,str] = "ID123"
print(identifier)
identifier = 1234
print(identifier)