import sys
input = sys.stdin.readline

L = int(input())
string = input()

def kmp(length, s):
    dp = [0 for _ in range(length + 1)]
    i = 1
    j = 0
    
    while i != length:
        if string[i] == string[j]:
            i, j = i + 1, j + 1
            dp[i] = j
        elif j == 0:
            i = i + 1
        else:
            j = dp[j]
    return dp[length]

print(L - kmp(L, string)) 