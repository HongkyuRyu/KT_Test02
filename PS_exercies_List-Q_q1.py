n = 1000
a = [False, False] + [True] * (n-1)
prime_nums = []

for i in range(2, n+1):
    if a[i]:
        prime_nums.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False
print(prime_nums)
print(len(prime_nums)) #소수 개수.