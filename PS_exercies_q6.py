# Q6 Answer template

def solution(n):
    answer = 0
    # 제곱근 구하기
    sqrt = n ** (1/2)
    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    else:
        return -1
