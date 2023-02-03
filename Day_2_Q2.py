# Q2 Answer template

def solution(numbers):
    answer = 0
    
    for i in range(0, 10):
        if i not in numbers:
            answer += i
    return answer

numbers = [5, 8, 4, 0, 6, 7, 9]
answer = solution(numbers)
print(answer)