# Q4 Answer Template

data = input('숫자로 이루어진 문자열을 입력하세요. ')
result = int(data[0]) # 첫번쨰 문자

for i in range (1, len(data)):
    next_num = int(data[i])
    if next_num <= 1 or result <= 1: #다음 숫자가 0 or 1 이거나, 지금까지 더한 값이 0 or 1이면
        result += next_num           # 더하는 것이 이득임.
    else:
        result *= next_num           # 나머지의 경우 곱하는 것이 더 커짐.
    

print(result)
