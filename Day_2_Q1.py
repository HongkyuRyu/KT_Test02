# Q1 Answer template

def solution(lottos, win_nums):
    answer = []
    rank = [(0,0),(1,6), (2,5), (3,4), (4,3), (5,2), (6,1), (6,0)]
    # 중복되는 값 미리 제거
    set1 = set(lottos)
    set2 = set(win_nums)
    same_number = len(set1 & set2)
    
    # 알아볼 수 없는 번호의 갯수: zero_cnt
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

# test case 1
lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
answer = solution(lottos, win_nums)
print(answer) # [3, 5] 출력됨.

# test case 2
lottos = [0, 0, 0, 0, 0, 0]
win_nums = [38, 19, 20, 40, 15, 25]
answer = solution(lottos, win_nums)
print(answer) # [1, 6] 출력됨.

# test case 3
lottos = [45, 4, 35, 20, 3, 9]
win_nums = [20, 9, 3, 45, 4, 35]
answer = solution(lottos, win_nums)
print(answer) # [1, 1] 출력됨.
