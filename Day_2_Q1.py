# Q1 Answer template

# version 1) 2021-09-17
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

# version 2: dic을 이용한 풀이 2023-02-03
def solution2(lottos, win_nums):
    # 0의 갯수 세기
    zeros = lottos.count(0)
    # 맞춘 갯수
    correct = 0
    # score 딕셔너리
    scores = {0: 6, 1:6, 2:5, 3:4, 4:3, 5:2, 6:1} # x개 맞춤: 순위
    
    for l in lottos:
        if l in win_nums:
            correct += 1
    
    best_rank = correct + zeros # 맞춘 갯수 + 0이 다 맞았다고 한다면 : 가장 높은 순위임.
    small_rank = correct # 맞춘 갯수만, 0은 다 틀렸다고 가정
    
    return [scores[best_rank], scores[small_rank]]




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
