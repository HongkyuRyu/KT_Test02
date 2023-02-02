import sys, math
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# prefix_gcd: 0부터 i까지의 gcd를 저장하는 리스트
# suffix_gcd: i부터 n-1까지의 gcd를 저장하는 리스트

pre_gcd = [0] * (n+1)
suf_gcd = [0] * (n+1)

pre_gcd[0] = arr[0]
for i in range(1, n):
    pre_gcd[i] = math.gcd(pre_gcd[i-1], arr[i])

for j in range(n-2, -1, -1):
    suf_gcd[j] = math.gcd(suf_gcd[j+1], arr[j])

answer = []
for i in range(n):
    # [0, i-1]까지 gcd
    front = pre_gcd[i-1]
    # [i+1, n-1]까지 gcd
    behind = suf_gcd[i+1]
    # result: i번째 수를 제외한 최종적인 gcd
    result = math.gcd(front, behind)
    if arr[i] % res == 0:
        continue
    answer.append((result, arr[i]))

answer.sort(reverse=True)
print(' '.join(map(str, ans[0])) if answer else -1)
