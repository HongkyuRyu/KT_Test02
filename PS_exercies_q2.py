import sys
input = sys.stdin.readline

n = int(input())
target = n
cnt = 0

while True:
    # 십의 자리, 일의 자리 분리 후, while문 돌면서, target값 업데이트
    target = (target % 10) * 10 + (target // 10 + target % 10) % 10
    cnt += 1
    # 종료조건
    if target == n:
        break
print(cnt)
