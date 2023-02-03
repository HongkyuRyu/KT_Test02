# Q5 Answer template
def solution(n, s): #n은 집합의 원소의 개수 , s: 원소의 합
    answer = []
    
    # 곱셈이 가장 큰 경우: 곱셈을 하는 두 숫자끼리 차이가 크지 않았을 때
    # ex) 1 * 8 < 4 * 5 < 4 * 4
    
    # 원소의 합 < 원소의 개수 (자연수로는 만들 수 없다.)
    if s < n:
        return [-1]
    
    # 숫자 골고루 분배해주기. n=2, s=9, 9//2 = 4 -> answer = [4, 4]
    for _ in range(n):
        answer.append(s//n)
    
    idx = 0
    
    for i in range(s-sum(answer)):
        answer[idx] += 1
        idx += 1
    answer.sort()
    return answer
        
n = 2
s = 9
answer = solution(n, s)
print(answer)