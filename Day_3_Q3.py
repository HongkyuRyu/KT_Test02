# Q3 answer template

def solution(store, customer):
    answer = []
    
    for i in customer:
        if i not in store:
            answer.append('no')
        else:
            answer.append('yes')
    return answer

store = [1,2,3,7,8]
customer = [1,5,8,4,6]
answer = solution(store, customer)
print(answer)