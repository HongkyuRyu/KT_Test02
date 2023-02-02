# Q3 Answer template

def solution(left, right):
    answer = 0
    
    for i in range(left, right+1):
        cnt = 0
        for j in range(1, i+1):
            if i % j == 0: # 약수의 갯수
                cnt += 1
        
        # 약수의 개수가 짝수인 경우
        if cnt % 2 == 0:
            answer += i
        else:
            answer -= i
    
    return answer

# ex)
left = 13
right = 17
c = solution(left, right)
print(c)
