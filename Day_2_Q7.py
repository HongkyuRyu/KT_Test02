# Q7 Answer Template

def solution(arr):
    answer = []
    answer.append(arr[0]) # 첫 문자 넣기.
    
    for i in range(1, len(arr)):
        flag = False
        
        if not flag and arr[i-1] != arr[i]:
            answer.append(arr[i])
            flag = True
    return answer

arr = [1,1,3,3,0,1,1]
#arr = [4,4,4,3,3]
answer = solution(arr)
print(answer)