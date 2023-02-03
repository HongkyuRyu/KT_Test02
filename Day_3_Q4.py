# Q4 Answer Template
import math

def lcm(a, b):
    return int(a * b / math.gcd(a, b))
    
def solution(arr):
    answer = 0
    temp = arr[0]
    for i in range(1, len(arr)):
        answer = lcm(arr[i], temp)
        temp = answer
        
    return answer

arr = [None]*15
arr = [1, 2,3]
answer = solution(arr)
print(answer)