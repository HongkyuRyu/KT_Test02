# Q1 Answer template

def solution(lottos, win_nums):
    answer = []
    rank = [(0,0),(1,6), (2,5), (3,4), (4,3), (5,2), (6,1), (6,0)]
    set1 = set(lottos)
    set2 = set(win_nums)
    same_number = len(set1 & set2)
    
    zero_cnt = 0
    for i in lottos:
        if i == 0:
            zero_cnt += 1
    
    for i in range(1, len(rank)):
        if rank[i][1] == same_number + zero_cnt:
            answer.append(rank[i][0])
    
    for i in range(1, len(rank)):
        if rank[i][1] == same_number:
            answer.append(rank[i][0])
    return answer

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
answer = solution(lottos, win_nums)
print(answer) # [3, 5] 출력됨.