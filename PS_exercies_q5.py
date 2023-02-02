# Q5 Answer Template

n = input('숫자를 입력하세요. ')
mid = len(n) // 2
left = n[:mid]
right = n[mid:]

l , r = 0, 0
for i in left:
    l += int(i)

for j in right:
    r += int(j)
if l == r:
    print("LUCKY")
else:
    print("READY")
