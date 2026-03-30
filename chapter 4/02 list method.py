import math

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 1

def solve(lst, k):
    Result = []
    n = len(lst)
    index = 0
    while index < n:
        chu = []
        for i in range(k):
            if index < n:
                chu.append(lst[index])
                index += 1
        Result.append(chu)
    print(Result)

solve(lst, k)
