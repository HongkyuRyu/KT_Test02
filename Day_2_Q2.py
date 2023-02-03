# Q2 Answer template

# 방법1
def solution(numbers):
    answer = 0
    
    for i in range(0, 10):
        if i not in numbers:
            answer += i
    return answer

numbers = [5, 8, 4, 0, 6, 7, 9]
answer = solution(numbers)
print(answer)


# 방법2
def solution2(numbers):
    answer = 45
    
    for i in range(0, 10):
        if i in numbers:
            answer -= i
    return answer
numbers = [5, 8, 4, 0, 6, 7, 9]
answer = solution2(numbers)
print(answer)